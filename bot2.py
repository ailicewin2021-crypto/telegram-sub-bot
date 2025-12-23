import telebot
import os

TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🤖 Bot Online!\nမြန်မာ Subtitle Bot အဆင်သင့်ပါ")

bot.infinity_polling()
