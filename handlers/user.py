from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from database import (
    register_user, get_user, get_favorites, remove_favorite,
    get_search_history, clear_history,
    get_language, set_language,
    get_user_downloads, check_daily_limit,
)
from utils.lang import t


async def cmd_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await register_user(user.id, user.username or "", user.first_name or "")
    lang = await get_language(user.id)
    await update.message.reply_text(
        t(lang, "welcome", name=user.first_name or "User"),
        parse_mode="HTML",
    )


async def cmd_help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = await get_language(update.effective_user.id)
    await update.message.reply_text(t(lang, "help"), parse_mode="HTML")


async def cmd_profile(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    lang    = await get_language(user_id)
    user    = await get_user(user_id)
    if not user:
        await update.message.reply_text("❌ Profil topilmadi.")
        return

    fav_count    = len(await get_favorites(user_id))
    downloads    = await get_user_downloads(user_id, limit=9999)
    dl_count     = len(downloads)
    _, remaining = await check_daily_limit(user_id)

    uname    = f"@{user['username']}" if user.get("username") else "—"
    lang_map = {"uz": "🇺🇿 O'zbek", "ru": "🇷🇺 Русский", "en": "🇬🇧 English"}
    user_lng = lang_map.get(user.get("language", "uz"), "🇺🇿 O'zbek")

    text = (
        f"👤 <b>Profilim</b>\n\n"
        f"🆔 ID:           <code>{user_id}</code>\n"
        f"👤 Ism:          <b>{user.get('first_name', '?')}</b>\n"
        f"📛 Username:     {uname}\n"
        f"🌍 Til:          {user_lng}\n\n"
        f"❤️ Sevimlilar:  <b>{fav_count}</b> ta\n"
        f"⬇️ Jami yuklab: <b>{dl_count}</b> ta\n"
        f"📅 Bugun qoldi: <b>{remaining}</b> ta\n\n"
        f"📅 Ro'yxatdan:  <code>{str(user.get('joined_at', '?'))[:10]}</code>"
    )
    await update.message.reply_text(text, parse_mode="HTML")


async def cmd_favorites(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    lang    = await get_language(user_id)
    favs    = await get_favorites(user_id)

    if not favs:
        await update.message.reply_text(t(lang, "favorites_empty"))
        return

    text     = "❤️ <b>Sevimlilar ro'yxati:</b>\n\n"
    keyboard = []
    for i, fav in enumerate(favs[:20], 1):
        title  = (fav.get("title") or "Unknown")[:40]
        artist = (fav.get("artist") or "Unknown")[:25]
        text  += f"{i}. <b>{title}</b>\n👤 {artist}\n\n"
        keyboard.append([
            InlineKeyboardButton(f"▶️ {i}. {title[:22]}", url=fav["url"]),
            InlineKeyboardButton("🗑 O'chir", callback_data=f"delfav_{fav['id']}"),
        ])
    if len(favs) > 20:
        text += f"<i>... va yana {len(favs) - 20} ta</i>"

    await update.message.reply_text(
        text,
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup(keyboard),
        disable_web_page_preview=True,
    )


async def cmd_history(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    lang    = await get_language(user_id)
    history = await get_search_history(user_id, 15)

    if not history:
        await update.message.reply_text(t(lang, "history_empty"))
        return

    text     = t(lang, "history_title") + "\n\n"
    keyboard = []
    for i, item in enumerate(history, 1):
        q = item["query"]
        text += f"{i}. {q}\n"
        keyboard.append([InlineKeyboardButton(f"🔍 {q[:35]}", callback_data=f"search_{q[:50]}")])
    keyboard.append([InlineKeyboardButton("🗑 Tarixni tozalash", callback_data="clear_history")])

    await update.message.reply_text(
        text, parse_mode="HTML", reply_markup=InlineKeyboardMarkup(keyboard))


async def cmd_lang(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = await get_language(update.effective_user.id)
    keyboard = InlineKeyboardMarkup([[
        InlineKeyboardButton("🇺🇿 O'zbek",  callback_data="setlang_uz"),
        InlineKeyboardButton("🇷🇺 Русский", callback_data="setlang_ru"),
        InlineKeyboardButton("🇬🇧 English", callback_data="setlang_en"),
    ]])
    await update.message.reply_text(t(lang, "lang_select"), reply_markup=keyboard)


async def cmd_cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data.clear()
    lang = await get_language(update.effective_user.id)
    await update.message.reply_text(t(lang, "cancelled"))


async def handle_delfav_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query   = update.callback_query
    user_id = query.from_user.id

    if query.data == "clear_history":
        await query.answer()
        await clear_history(user_id)
        try:
            await query.edit_message_text("🗑 Qidiruv tarixi tozalandi!")
        except Exception:
            pass
        return

    await query.answer()
    try:
        fav_id = int(query.data.split("_", 1)[1])
        await remove_favorite(fav_id, user_id)
        await query.answer("🗑 Sevimlilardan o'chirildi!", show_alert=False)
        try:
            await query.edit_message_reply_markup(reply_markup=None)
        except Exception:
            pass
    except Exception:
        await query.answer("❌ Xatolik")


async def handle_setlang_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query    = update.callback_query
    user_id  = query.from_user.id
    new_lang = query.data.split("_", 1)[1]
    await query.answer()
    await set_language(user_ **...**

_This response is too long to display in full._
