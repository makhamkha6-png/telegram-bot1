from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    ApplicationBuilder,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
)

# بيانات البوت والروابط الرسمية
TOKEN = "8844323559:AAGOzdTiT15CsyqlY4CqLLQbKxdYP-a83Z8"
TARGET_LINK = "https://t.me/pNKD4eoeWmExYzg0"
TIKTOK_LINK = "https://www.tiktok.com/@za9zo9i_z1"
INSTA_LINK = "https://www.instagram.com/am.httx/?hl=en"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_first_name = update.effective_user.first_name
    bot_name = context.bot.first_name
    
    keyboard = [
        [InlineKeyboardButton("🍏 بوت لعبة التفاحة (توقعات)", callback_data="service_apple")],
        [InlineKeyboardButton("📊 توقعات 1XBET", callback_data="service_1xbet")],
        [InlineKeyboardButton("🎵 بيع حسابات تيك توك", callback_data="service_tiktok")],
        [InlineKeyboardButton("📸 بيع حسابات انستغرام", callback_data="service_instagram")],
        [InlineKeyboardButton("👻 خدمات سناب بلس", callback_data="service_snap")],
        [InlineKeyboardButton("💳 طرق الدفع (CCP / BaridiMob)", callback_data="payment_info")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    welcome_text = (
        f"أهلاً وسهلاً بك يا <b>{user_first_name}</b> 👋\n\n"
        f"يسعدني انضمامك إلى <b>{bot_name}</b> 🚀\n"
        f"كيف يمكنني مساعدتك اليوم؟ اختر إحدى الخدمات التالية للبدء:"
    )
    
    await update.message.reply_text(welcome_text, parse_mode="HTML", reply_markup=reply_markup)

async def handle_button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    
    data = query.data
    
    if data == "service_apple":
        text = (
            "🍏 <b>توقعات لعبة التفاحة (1XBET)</b>\n\n"
            "للحصول على التوقعات والسكربت الخاص بلعبة التفاحة، يرجى التواصل معنا مباشرة عبر حساباتنا الرسمية على تيك توك أو انستغرام:\n\n"
            "اختر المنصة التي تفضلها بالأسفل للتواصل السريع:"
        )
        keyboard = [
            [InlineKeyboardButton("🎵 التواصل عبر TikTok", url=TIKTOK_LINK)],
            [InlineKeyboardButton("📸 التواصل عبر Instagram", url=INSTA_LINK)],
            [InlineKeyboardButton("💬 التواصل عبر القناة الرسمية", url=TARGET_LINK)],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.reply_text(text, parse_mode="HTML", reply_markup=reply_markup)

    elif data == "service_1xbet":
        text = (
            "📊 <b>توقعات 1XBET</b>\n\n"
            "نوفر لك يومياً أهم التوقعات والتحليلات الرياضية ونسب الفوز المرتفعة.\n\n"
            "تواصل معنا عبر حساباتنا الرسمية للحصول على التوقعات:"
        )
        keyboard = [
            [InlineKeyboardButton("🎵 TikTok", url=TIKTOK_LINK), InlineKeyboardButton("📸 Instagram", url=INSTA_LINK)],
            [InlineKeyboardButton("📩 التواصل المباشر", url=TARGET_LINK)]
        ]
        await query.message.reply_text(text, parse_mode="HTML", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data == "service_tiktok":
        text = (
            "🎵 <b>بيع حسابات تيك توك</b>\n\n"
            "حسابات متفاعلة وجاهزة للبيع بمختلف أعداد المتابعين وبأسعار مناسبة.\n\n"
            "تفضل بزيارة حسابنا أو التواصل معنا للشراء:"
        )
        keyboard = [
            [InlineKeyboardButton("🎵 زيارة حساب TikTok", url=TIKTOK_LINK)],
            [InlineKeyboardButton("📩 التواصل للشراء", url=TARGET_LINK)]
        ]
        await query.message.reply_text(text, parse_mode="HTML", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data == "service_instagram":
        text = (
            "📸 <b>بيع حسابات انستغرام</b>\n\n"
            "حسابات انستغرام حقيقية ومتفاعلة متاحة للبيع وضمان كامل."
        )
        keyboard = [
            [InlineKeyboardButton("📸 زيارة حساب Instagram", url=INSTA_LINK)],
            [InlineKeyboardButton("📩 التواصل للشراء", url=TARGET_LINK)]
        ]
        await query.message.reply_text(text, parse_mode="HTML", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data == "service_snap":
        text = (
            "👻 <b>خدمات سناب بلس</b>\n\n"
            "اشتراكات سناب شات بلس بمميزات حصرية وتفعيل سريع وآمن."
        )
        keyboard = [
            [InlineKeyboardButton("🎵 TikTok", url=TIKTOK_LINK), InlineKeyboardButton("📸 Instagram", url=INSTA_LINK)],
            [InlineKeyboardButton("📩 التواصل للطلب", url=TARGET_LINK)]
        ]
        await query.message.reply_text(text, parse_mode="HTML", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data == "payment_info":
        text = (
            "💳 <b>طرق الدفع المتاحة:</b>\n\n"
            "• <b>BaridiMob (بريدي موب)</b>\n"
            "• <b>CCP (الحساب البريدي)</b>\n\n"
            "لطلب رقم الحساب وتأكيد الدفع، تواصل معنا عبر تيك توك أو انستغرام:"
        )
        keyboard = [
            [InlineKeyboardButton("🎵 TikTok", url=TIKTOK_LINK), InlineKeyboardButton("📸 Instagram", url=INSTA_LINK)],
            [InlineKeyboardButton("📩 طلب رقم الحساب", url=TARGET_LINK)]
        ]
        await query.message.reply_text(text, parse_mode="HTML", reply_markup=InlineKeyboardMarkup(keyboard))

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_button))
    
    print("البوت يعمل الآن بدون أي أخطاء...")
    app.run_polling()
