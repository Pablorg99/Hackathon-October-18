#!/usr/bin/env python
# -*- coding: utf-8 -*-

import spotipy
import spotipy.util as util
import telebot
from flask import request
from libs import private as TOKEN
from libs import credentials as cred

bot = telebot.TeleBot(TOKEN.token)

@bot.message_handler(commands=['log_in'])
def logIn(message):
	cid = message.chat.id
	scope = 'playlist-modify-private'
	bot.send_message(cid ,'Bienvenido a SBotify')
	bot.send_message(cid, 'Dime tu nombre de usuario de Spotify')
	@bot.message_handler(func = lambda message: True)
	def getUsername(message):
		username = str(message)
		tk = util.prompt_for_user_token(username, scope, cred.client_id, cred.client_secret, cred.redirect_uri)
		sp = spotipy.Spotify(auth = tk)

bot.polling()
