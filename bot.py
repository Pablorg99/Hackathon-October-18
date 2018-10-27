import spotipy
import telebot
from libs import private as token

bot = telebot.TeleBot(token)
sp = spotipy.Spotify()


@bot.message_handler(commands=['setplaylist'])
def setplaylist(message):
	bot.reply_to(message, "Howdy, how are you doing?")