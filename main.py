import telegram
from telegram.ext import Application, CommandHandler

# Bot tokenini dosyadan okuyun
with open("Token.txt", "r") as f:
    TOKEN = f.read().strip()  # API bağlantısı

# /start komutu için yanıt fonksiyonu

async def start(update, context):
    await update.message.reply_text("<b>Merhaba, Hoşgeldiniz.</b>", parse_mode='HTML')

async def youtube(update, context):
    await update.message.reply_text("<b> Youtube : https://www.youtube.com/@caglar8901 </b>", parse_mode='HTML')

async def instagram(update, context):
    await update.message.reply_text("<b> İnstagram : https://www.instagram.com/caglarcetin_/ </b>", parse_mode='HTML')

async def GitHub(update, context):
    await update.message.reply_text("<b> GitHub : https://github.com/cagscet </b>", parse_mode='HTML')

async def Linkedin(update, context):
    await update.message.reply_text("<b> Linkedin : https://www.linkedin.com/in/caglarcetin/ </b>", parse_mode='HTML')

async def komutlar(update, context):
    await update.message.reply_text("<b>Komutlar :\nstart \nyoutube \ninstagram \nGitHub \nLinkedin </b>", parse_mode='HTML')

# Updater ve Dispatcher oluşturma (yeni sürüme uygun)
application = Application.builder().token(TOKEN).build()

# komutları işleyiciye ekleme
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("youtube", youtube))
application.add_handler(CommandHandler("instagram", instagram))
application.add_handler(CommandHandler("GitHub", GitHub))
application.add_handler(CommandHandler("Linkedin", Linkedin))
application.add_handler(CommandHandler("Komutlar", komutlar))

# Botu başlatma

application.run_polling()


