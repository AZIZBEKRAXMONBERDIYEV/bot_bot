from telegram import Bot
TOKEN="6354682365:AAFbm5e6TnyQtgVpUMrFZrQ7P6rRmjsz17k"

bot=Bot(token=TOKEN)

print(bot.set_webhook("https://ferda.pythonanywhere.com/"))