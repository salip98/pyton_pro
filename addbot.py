from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# /start komutu için cevap
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Merhaba! Ben akıllı Telegram botuyum. Bana bir şey yaz, cevaplayayım!")

# Metin mesajlarını analiz eden fonksiyon
async def cevap_ver(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mesaj = update.message.text.lower()

    if "merhaba" in mesaj or "selam" in mesaj:
        yanit = "Merhaba! Nasılsın?"
    elif "nasılsın" in mesaj:
        yanit = "Ben bir botum ama gayet iyiyim 🙂 Sen nasılsın?"
    elif "adın ne" in mesaj:
        yanit = "Ben Python ile yazılmış bir Telegram botuyum. Henüz bir adım yok 🙃"
    elif "hava nasıl" in mesaj:
        yanit = "Benim bulunduğum sunucuda hep güzel 😎"
    elif "teşekkür" in mesaj:
        yanit = "Rica ederim! Yardımcı olabildiysem ne mutlu 😊"
    else:
        yanit = "Hmm... Bunu tam anlayamadım. Başka bir şey sormak ister misin?"

    await update.message.reply_text(yanit)
async def topla(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args=context.args
    if len(args)!=2:
        await update.message.reply_text("Lütfen iki sayı giriniz. örnek:/topla 4 8")
        return
    try:
        sayi1=float(args[0])
        sayi2=float(args[1])
        toplam=sayi1+sayi2
        await update.message.reply_text(f"toplam:{toplam}")
    except ValueError:
        await update.message.reply_text("Lütfen iki sayı giriniz. örnek:/topla 4 8")

# Botu çalıştır
app = ApplicationBuilder().token("7726858645:AAEDWnsW1SZTW7DNTg4gsLQXgeb9lAoXQac").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("topla", topla))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, cevap_ver))

app.run_polling()
