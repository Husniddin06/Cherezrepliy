TEXTS: dict = {
    "uz": {
        "welcome": (
            "👋 Salom, <b>{name}</b>!\n\n"
            "🎵 Men musiqa va media yuklovchi botman.\n\n"
            "📌 <b>Nima qila olaman:</b>\n"
            "• Qo'shiq nomi yoki artist bo'yicha qidirish\n"
            "• YouTube va TikTok dan yuklab olish\n"
            "• MP3 va Video formatida yuborish\n"
            "• Sevimlilar va tarix saqlash\n\n"
            "🎶 Qo'shiq nomini yozing yoki link yuboring!"
        ),
        "help": (
            "📖 <b>Yordam</b>\n\n"
            "🎵 <b>Musiqa qidirish:</b>\n"
            "• Qo'shiq nomini yozing\n"
            "• Artist ismini yozing\n\n"
            "🔗 <b>Link orqali yuklab olish:</b>\n"
            "• YouTube linkini yuboring\n"
            "• TikTok linkini yuboring\n\n"
            "📋 <b>Buyruqlar:</b>\n"
            "/start     — Botni boshlash\n"
            "/help      — Yordam\n"
            "/favorites — ❤️ Sevimlilar\n"
            "/history   — 📜 Qidiruv tarixi\n"
            "/profile   — 👤 Profilim\n"
            "/trending  — 🔥 Trend qo'shiqlar\n"
            "/lang      — 🌍 Til tanlash\n"
            "/cancel    — ❌ Bekor qilish\n\n"
            "📅 Kunlik limit: <b>30 ta yuklab olish</b>"
        ),
        "searching":         "🔍 Qidirilmoqda...",
        "no_results":        "❌ Hech narsa topilmadi. Boshqa so'z bilan urinib ko'ring.",
        "select_song":       "🎵 Natijalardan birini tanlang:",
        "downloading_audio": "⬇️ MP3 yuklanmoqda...",
        "downloading_video": "⬇️ Video yuklanmoqda...",
        "processing":        "⏳ Ishlanmoqda...",
        "download_failed":   "❌ Yuklashda xatolik. Keyinroq urinib ko'ring.",
        "file_too_large":    "❌ Fayl 50MB dan katta.",
        "getting_info":      "⏳ Ma'lumot olinmoqda...",
        "link_detected": (
            "🔗 <b>Link aniqlandi!</b>\n\n"
            "🎵 <b>{title}</b>\n"
            "👤 {uploader}\n\n"
            "Nimani yuklashni xohlaysiz?"
        ),
        "link_invalid":            "❌ Link noto'g'ri yoki qo'llab-quvvatlanmaydi.",
        "platform_login_required": "❌ Instagram yuklab olish uchun login talab qiladi.\n\nYouTube yoki TikTok linkini yuboring.",
        "favorites_empty":  "❤️ Sevimlilar ro'yxati bo'sh.",
        "favorites_added":  "❤️ Sevimlilar ro'yxatiga qo'shildi!",
        "favorites_exists": "ℹ️ Bu qo'shiq allaqachon sevimlilaringizda.",
        "history_empty":    "📜 Qidiruv tarixi bo'sh.",
        "history_title":    "📜 <b>So'nggi qidiruvlar:</b>",
        "rate_limited":     "⚠️ Iltimos, {wait} soniya kuting.",
        "daily_limit":      "📅 Kunlik limitingiz tugadi (30 ta). Ertaga qayta urinib ko'ring.",
        "banned":           "🚫 Siz botdan bloklangansiz.",
        "cancelled":        "❌ Bekor qilindi.",
        "lang_select":      "🌍 Tilni tanlang:",
        "lang_changed":     "✅ Til o'zgartirildi!",
        "playlist_start":   "📋 Playlist yuklanmoqda (max 10 ta qo'shiq)...",
        "playlist_done":    "✅ Playlist yuklandi!",
        "btn_audio":        "🎧 MP3",
        "btn_video":        "🎥 Video",
        "page_info":        "📄 {current}/{total}",
    },

    "ru": {
        "welcome": (
            "👋 Привет, <b>{name}</b>!\n\n"
            "🎵 Я бот для скачивания музыки и медиа.\n\n"
            "📌 <b>Что я умею:</b>\n"
            "• Поиск по названию или исполнителю\n"
            "• Скачивание с YouTube и TikTok\n"
            "• Отправка в MP3 и видео форматах\n"
            "• Сохранение избранного и истории\n\n"
            "🎶 Напишите название или отправьте ссылку!"
        ),
        "help": (
            "📖 <b>Помощь</b>\n\n"
            "🎵 <b>Поиск музыки:</b>\n"
            "• Введите название песни\n"
            "• Введите имя исполнителя\n\n"
            "🔗 <b>Скачивание по ссылке:</b>\n"
            "• Отправьте ссылку YouTube\n"
            "• Отправьте ссылку TikTok\n\n"
            "📋 <b>Команды:</b>\n"
            "/start     — Начало\n"
            "/help      — Помощь\n"
            "/favorites — ❤️ Избранное\n"
            "/history   — 📜 История\n"
            "/profile   — 👤 Профиль\n"
            "/trending  — 🔥 Тренды\n"
            "/lang      — 🌍 Язык\n"
            "/cancel    — ❌ Отмена\n\n"
            "📅 Дневной лимит: <b>30 загрузок</b>"
        ),
        "searching":         "🔍 Поиск...",
        "no_results":        "❌ Ничего не найдено. Попробуйте другой запрос.",
        "select_song":       "🎵 Выберите из результатов:",
        "downloading_audio": "⬇️ Скачиваю MP3...",
        "downloading_video": "⬇️ Скачиваю видео...",
        "processing":        "⏳ Обработка...",
        "download_failed":   "❌ Ошибка загрузки. Попробуйте позже.",
        "file_too_large":    "❌ Файл больше 50МБ.",
        "getting_info":      "⏳ Получаю информацию...",
        "link_detected": (
            "🔗 <b>Ссылка обнаружена!</b>\n\n"
            "🎵 <b>{title}</b>\n"
            "👤 {uploader}\n\n"
            "Что скачать?"
        ),
        "link_invalid":            "❌ Ссылка недействительна или не поддерживается.",
        "platform_login_required": "❌ Instagram требует авторизации.\n\nОтправьте ссылку YouTube или TikTok.",
        "favorites_empty":  "❤️ Список избранного пуст.",
        "favorites_added":  "❤️ Добавлено в избранное!",
        "favorites_exists": "ℹ️ Эта песня уже в избранном.",
        "history_empty":    "📜 История поиска пуста.",
        "history_title":    "📜 <b>Последние запросы:</b>",
        "rate_limited":     "⚠️ Подождите {wait} секунд.",
        "daily_limit":      "📅 Дневной лимит исчерпан (30 шт). Попробуйте завтра.",
        "banned":           "🚫 Вы заблокированы.",
        "cancelled":        "❌ Отменено.",
        "lang_select":      "🌍 Выберите язык:",
        "lang_changed":     "✅ Язык изменён!",
        "playlist_start":   "📋 Загружаю плейлист (макс. 10 треков)...",
        "playlist_done":    "✅ Плейлист загружен!",
        "btn_audio":        "🎧 MP3",
        "btn_video":        "🎥 Видео",
        "page_info":        "📄 {current}/{total}",
    },

    "en": {
        "welcome": (
            "👋 Hello, <b>{name}</b>!\n\n"
            "🎵 I'm a music & media downloader bot.\n\n"
            "📌 <b>What I can do:</b>\n"
            "• Search by song title or artist\n"
            "• Download from YouTube and TikTok\n"
            "• Send in MP3 and video formats\n"
            "• Save favorites and history\n\n"
            "🎶 Type a song name or send a link!"
        ),
        "help": (
            "📖 <b>Help</b>\n\n"
            "🎵 <b>Music Search:</b>\n"
            "• Type a song name\n"
            "• Type an artist name\n\n"
            "🔗 <b>Link Download:</b>\n"
            "• Send a YouTube link\n"
            "• Send a TikTok link\n\n"
            "📋 <b>Commands:</b>\n"
            "/start     — Start\n"
            "/help      — Help\n"
            "/favorites — ❤️ Favorites\n"
            "/history   — 📜 History\n"
            "/profile   — 👤 My Profile\n"
            "/trending  — 🔥 Trending\n"
            "/lang      — 🌍 Language\n"
            "/cancel    — ❌ Cancel\n\n"
            "📅 Daily limit: <b>30 downloads</b>"
        ),
        "searching":         "🔍 Searching...",
        "no_results":        "❌ Nothing found. Try a different query.",
        "select_song":       "🎵 Select from results:",
        "downloading_audio": "⬇️ Downloading MP3...",
        "downloading_video": "⬇️ Downloading video...",
        "processing":        "⏳ Processing...",
        "download_failed":   "❌ Download failed. Try again later.",
        "file_too_large":    "❌ File is over 50MB.",
        "getting_info":      "⏳ Getting info...",
        "link_detected": (
            "🔗 <b>Link detected!</b>\n\n"
            "🎵 <b>{title}</b>\n"
            "👤 {uploader}\n\n"
            "What to download?"
        ),
        "link_invalid":            "❌ Invalid or unsupported link.",
        "platform_login_required": "❌ Instagram requires login.\n\nSend a YouTube or TikTok link.",
        "favorites_empty":  "❤️ Favorites list is empty.",
        "favorites_added":  "❤️ Added to favorites!",
        "favorites_exists": "ℹ️ This song is already in favorites.",
        "history_empty":    "📜 Search history is empty.",
        "history_title":    "📜 <b>Recent searches:</b>",
        "rate_limited":     "⚠️ Please wait {wait} seconds.",
        "daily_limit":      "📅 Daily download limit reached (30). Try again tomorrow.",
        "banned":           "🚫 You are banned from this bot.",
        "cancelled":        "❌ Cancelled.",
        "lang_select":      "🌍 Select language:",
        "lang_changed":     "✅ Language changed!",
        "playlist_start":   "📋 Downloading playlist (max 10 tracks)...",
        "playlist_done":    "✅ Playlist downloaded!",
        "btn_audio":        "🎧 MP3",
        "btn_video":        "🎥 Video",
        "page_info":        "📄 {current}/{total}",
    },
}


def t(lang: str, key: str, **kwargs) -> str:
    text = (
        TEXTS.get(lang, TEXTS["uz"]).get(key)
        or TEXTS["uz"].get(key)
        or key
    )
    if kwargs:
        try:
            return text.format(**kwargs)
        except Exception:
            return text
    return text


def format_duration(seconds: int) -> str:
    if not seconds or seconds <= 0:
        return ""
    m, s = divmod(int(seconds), 60)
    h, m = divmod(m, 60)
    if h:
        return f"{h}:{m:02d}:{s:02d}"
    return f"{m}:{s:02d}"
