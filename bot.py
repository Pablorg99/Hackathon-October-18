import spotipy
import telebot
from libs import private as token

bot = telebot.TeleBot(token)
sp = spotipy.Spotify()

@bot.message_handler(commands=['start'])
def send_welcome(message):
	sendMessage(message.chat.id ,'Bienvenido a SBotify')

bot.polling()
