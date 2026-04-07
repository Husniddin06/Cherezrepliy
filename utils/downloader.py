import os
import re
import uuid
import asyncio
import time
import aiohttp
import yt_dlp
from typing import Optional, List, Dict

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
TEMP_DIR = os.path.join(BASE_DIR, "temp_downloads")
os.makedirs(TEMP_DIR, exist_ok=True)

MAX_FILE_SIZE = 50 * 1024 * 1024

_INNERTUBE_URL = (
    "https://www.youtube.com/youtubei/v1/search"
    "?key=AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8"
)
_INNERTUBE_CTX = {
    "client": {
        "clientName": "WEB",
        "clientVersion": "2.20240101.00.00",
        "hl": "en",
        "gl": "US",
    }
}

_SEARCH_CACHE: Dict[str, tuple] = {}
CACHE_TTL = 3600


def detect_platform(url: str) -> Optional[str]:
    u = url.lower()
    if "youtube.com" in u or "youtu.be" in u:
        return "youtube"
    if "instagram.com" in u:
        return "instagram"
    if "tiktok.com" in u:
        return "tiktok"
    if "vk.com" in u:
        return "vk"
    return None


def is_url(text: str) -> bool:
    return bool(re.match(r"https?://\S+", text.strip()))


def _parse_duration(text: str) -> int:
    if not text:
        return 0
    try:
        parts = [int(p) for p in text.split(":")]
        if len(parts) == 2:
            return parts[0] * 60 + parts[1]
        if len(parts) == 3:
            return parts[0] * 3600 + parts[1] * 60 + parts[2]
    except Exception:
        pass
    return 0


def _parse_innertube(data: dict) -> List[Dict]:
    results = []
    try:
        sections = (
            data.get("contents", {})
            .get("twoColumnSearchResultsRenderer", {})
            .get("primaryContents", {})
            .get("sectionListRenderer", {})
            .get("contents", [])
        )
        for section in sections:
            items = section.get("itemSectionRenderer", {}).get("contents", [])
            for item in items:
                vr = item.get("videoRenderer")
                if not vr:
                    continue
                vid_id = vr.get("videoId", "")
                if not vid_id:
                    continue
                title_runs = vr.get("title", {}).get("runs", [])
                title = title_runs[0]["text"] if title_runs else "Unknown"
                upl_runs = (
                    vr.get("ownerText", {}).get("runs", [])
                    or vr.get("shortBylineText", {}).get("runs", [])
                )
                uploader = upl_runs[0]["text"] if upl_runs else "Unknown"
                dur_text = vr.get("lengthText", {}).get("simpleText", "")
                results.append({
                    "title":    title,
                    "uploader": uploader,
                    "duration": _parse_duration(dur_text),
                    "url":      f"https://www.youtube.com/watch?v={vid_id}",
                    "id":       vid_id,
                })
                if len(results) >= 8:
                    return results
    except Exception:
        pass
    return results


async def search_music(query: str, limit: int = 8) -> List[Dict]:
    key = query.lower().strip()
    if key in _SEARCH_CACHE:
        val, exp = _SEARCH_CACHE[key]
        if time.time() < exp:
            return val
    results = await _search_innertube(query)
    if not results:
        results = await _search_ydl(query, limit)
    if results:
        _SEARCH_CACHE[key] = (results, time.time() + CACHE_TTL)
    return results


async def _search_innertube(query: str) -> List[Dict]:
    try:
        payload = {
            "context": _INNERTUBE_CTX,
            "query":   query,
            "params":  "EgIQAQ%3D%3D",
        }
        headers = {
            "Content-Type": "application/json",
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            ),
        }
        timeout = aiohttp.ClientTimeout(total=6)
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.post(
                _INNERTUBE_URL, json=payload, headers=headers
            ) as resp:
                if resp.status == 200:
                    data = await resp.json(content_type=None)
                    return _parse_innertube(data)
    except Exception:
        pass
    return []


async def _search_ydl(query: str, limit: int = 8) -> List[Dict]:
    loop = asyncio.get_running_loop()

    def _run():
        opts = {
            "quiet":          True,
            "no_warnings":    True,
            "skip_download":  True,
            "extract_flat":   "in_playlist",
            "socket_timeout": 10,
            "retries":        1,
        }
        try:
            with yt_dlp.YoutubeDL(opts) as ydl:
                res = ydl.extract_info(f"ytsearch{limit}:{query}", download=False)
            out = []
            for e in (res.get("entries", []) if res else []):
                if not e:
                    continue
                vid = e.get("id") or ""
                if not vid:
                    continue
                out.append({
                    "title":    e.get("title", "Unknown"),
                    "uploader": e.get("uploader") or e.get("channel", "Unknown"),
                    "duration": e.get("duration", 0),
                    "url":      f"https://www.youtube.com/watch?v={vid}",
                    "id":       vid,
                })
            return out
        except Exception:
            return []

    return await loop.run_in_executor(None, _run)


async def get_video_info(url: str) -> Optional[Dict]:
    loop = asyncio.get_running_loop()

    def _run():
        opts = {
            "quiet":          True,
            "no_warnings":    True,
            "skip_download":  True,
            "noplaylist":     True,
            "socket_timeout": 15,
            "retries":        2,
        }
        if detect_platform(url) == "tiktok":
            opts["http_headers"] = {"User-Agent": _tiktok_ua()}
        try:
            with yt_dlp.YoutubeDL(opts) as ydl:
                info = ydl.extract_info(url, download=False)
                if not info:
                    return None
                return {
                    "title":    info.get("title", "Unknown"),
                    "uploader": info.get("uploader") or info.get("channel", "Unknown"),
                    "duration": info.get("duration", 0),
                    "url":      url,
                }
        except Exception:
            return None

    return await loop.run_in_executor(None, _run)


def _find_file(uid: str, ext: str = None) -> Optional[str]:
    best, best_size = None, 0
    try:
        for f in os.listdir(TEMP_DIR):
            if not f.startswith(uid):
                continue
            if ext and not f.endswith(ext):
                continue
            full = os.path.join(TEMP_DIR, f)
            try:
                size = os.path.getsize(full)
            except Exception:
                continue
            if size > best_size:
                best_size = size
                best = full
        if best and best_size <= MAX_FILE_SIZE:
            return best
    except Exception:
        pass
    return None


def _tiktok_ua() -> str:
    return (
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) "
        "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 "
        "Mobile/15E148 Safari/604.1"
    )


async def download_audio(url: str, title: str = "audio") -> Optional[str]:
    loop = asyncio.get_running_loop()

    def _run():
        uid = uuid.uuid4().hex[:10]
        outtmpl = os.path.join(TEMP_DIR, f"{uid}.%(ext)s")
        opts = {
            "quiet":                         True,
            "no_warnings":                   True,
            "noplaylist":                    True,
            "format":                        "bestaudio[ext=m4a]/bestaudio[ext=webm]/bestaudio/best",
            "outtmpl":                       outtmpl,
            "socket_timeout":                30,
            "retries":                       3,
            "fragment_retries":              3,
            "concurrent_fragment_downloads": 4,
            "postprocessors": [{
                "key":              "FFmpegExtractAudio",
                "preferredcodec":   "mp3",
                "preferredquality": "192",
            }],
        }
        if detect_platform(url) == "tiktok":
            opts["http_headers"] = {"User-Agent": _tiktok_ua()}
        try:
            with yt_dlp.YoutubeDL(opts) as ydl:
                ydl.extract_info(url, download=True)
            return _find_file(uid, ".mp3") or _find_file(uid)
        except Exception:
            return None

    return await loop.run_in_executor(None, _run)


async def download_video(url: str, title: str = "video") -> Optional[str]:
    loop = asyncio.get_running_loop()

    def _run():
        uid = uuid.uuid4().hex[:10]
        outtmpl = os.path.join(TEMP_DIR, f"{uid}.%(ext)s")
        opts_base = {
            "quiet":                         True,
            "no_warnings":                   True,
            "noplaylist":                    True,
            "outtmpl":                       outtmpl,
            "socket_timeout":                30,
            "retries":                       3,
            "fragment_retries":              3,
            "concurrent_fragment_downloads": 4,
            "merge_output_format":           "mp4",
        }
        if detect_platform(url) == "tiktok":
            opts_base["http_headers"] = {"User-Agent": _tiktok_ua()}
        formats = [
            "bestvideo[height<=720][ext=mp4]+bestaudio[ext=m4a]/bestvideo[height<=720]+bestaudio/best[height<=720]",
            "bestvideo[ext=mp4]+bestaudio/best[ext=mp4]/best",
            "best",
        ]
        for fmt in formats:
            try:
                with yt_dlp.YoutubeDL({**opts_base, "format": fmt}) as ydl:
                    ydl.extract_info(url, download=True)
                f = _find_file(uid, ".mp4") or _find_file(uid)
                if f:
                    return f
            except Exception:
                continue
        return None

    return await loop.run_in_executor(None, _run)


async def download_playlist(url: str) -> List[str]:
    loop = asyncio.get_running_loop()

    def _run():
        uid = uuid.uuid4().hex[:10]
        opts = {
            "quiet":          True,
            "no_warnings":    True,
            "noplaylist":     False,
            "playlistend":    10,
            "format":         "bestaudio[ext=m4a]/bestaudio/best",
            "outtmpl":        os.path.join(TEMP_DIR, f"{uid}_%(playlist_index)02d.%(ext)s"),
            "socket_timeout": 30,
            "retries":        3,
            "postprocessors": [{
                "key":              "FFmpegExtractAudio",
                "preferredcodec":   "mp3",
                "preferredquality": "192",
            }],
        }
        try:
            with yt_dlp.YoutubeDL(opts) as ydl:
                ydl.extract_info(url, download=True)
            return [
                os.path.join(TEMP_DIR, f)
                for f in sorted(os.listdir(TEMP_DIR))
                if f.startswith(uid) and f.endswith(".mp3")
                and os.path.getsize(os.path.join(TEMP_DIR, f)) <= MAX_FILE_SIZE
            ]
        except Exception:
            return []

    return await loop.run_in_executor(None, _run)


def cleanup_file(path: str):
    try:
        if path and os.path.exists(path):
            os.remove(path)
    except Exception:
        pass


def cleanup_old_files(max_age_seconds: int = 3600):
    now = time.time()
    try:
        for f in os.listdir(TEMP_DIR):
            full = os.path.join(TEMP_DIR, f)
            if os.path.isfile(full) and now - os.path.getmtime(full) > max_age_seconds:
                os.remove(full)
    except Exception:
        pass
