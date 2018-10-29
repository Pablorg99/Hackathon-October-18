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

# @app.route('/auth')
# def spotify_authentication():
#     """
#     Inicia la fase 1 de autenticación OAuth2 con spotify
#     Manda el navegador del usuario a autenticarse contra Spotify
#     """
#     scope = "playlist-modify-private"
#     oauth = SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI, scope=scope)
# 
#     return redirect(oauth.get_authorize_url())
# 
# @app.route('/spotify')
# def spotify_authorization():
#     """
#     Si la autenticación tiene éxito vuelve a esta URL:
#         http://localhost/spotify
#     """
#     scope = "playlist-modify-private"
#     oauth = SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI, scope=scope)
# 
#     code = oauth.parse_response_code(url=request.url)
#     if code:
#         # token es un diccionario
#         # token['access_token'] contiene el token de acceso a la API de spotify
#         token = oauth.get_access_token(code)
# 
#         # Aqui deberíamos enviar el token al bot a través del navegador del usuario para que lo asocie
#         # El bot pilla el token como parámetro del comando start y lo asocia al usuario de Telegram
#         # return redirect(https://tg.me/mibot?start=access_token)
# 
#         # El access token se usa para acceder a la API de Spotify
#         sp = Spotify(auth=token['access_token'])
#         user = sp.current_user()
# 
#         return json.dumps(user, ensure_ascii=False), 200
# 
#     return "Error de autenticación", 400
