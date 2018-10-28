#!/usr/bin/env python
# -*- coding: utf-8 -*-

# python library for Spotify Web Api
import spotipy
import spotipy.util as util
# python library for Telegram Bot Api
import telebot
# needed for argv
import sys
# file with Telegram bot token and client credentials
from libs import private as pr

bot = telebot.TeleBot(pr.token)

@bot.message_handler(commands = ['start'])
def welcomeMessage(message):
	bot.reply_to(message ,'Bienvenido a SBotify, usa /log_in para loguearte en spotify')

@bot.message_handler(commands = ['log_in'])
def logIn(message):
	username = 'bot.py'
	scope = 'playlist-modify-private'
	tk = util.prompt_for_user_token(username, scope, pr.client_id, pr.client_secret, pr.redirect_uri)

	if tk:
		sp = spotipy.Spotify(auth = tk)
		#Test with an example from Spotipy doc
		results = sp.current_user_saved_tracks()
		for item in results['items']:
			track = item['track']
			print track['name'] + ' - ' + track['artists'][0]['name']		
	else:
   		print "Can't get token for", username

bot.polling()
