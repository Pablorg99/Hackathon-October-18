import spotipy
import spotipy.util as util
import telebot
from libs import private as token
from libs import credentials as cred
from libs import functions as func

bot = telebot.TeleBot(token)
sp = spotipy.Spotify()

@bot.message_handler(commands=['log_in'])
def send_welcome(message):
	cid = message.chat.id
	bot.send_message(cid ,'Bienvenido a SBotify')
	bot.send_message(cid, 'Dime tu nombre de usuario')
	#username = func.catch_username(message)

#util.prompt_for_user_token(username, 'playlist-modify-private', )

bot.polling()
