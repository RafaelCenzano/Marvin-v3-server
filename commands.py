#Imports
from os import system, path # run terminal commands and find files in path
from json import load, dump # import json load
from difflib import get_close_matches # import close matches functions
from datetime import datetime # import datetime to show date and time
from threading import Thread # import threading to run more than one job at a time
from api import ApiService # classes to handle api work
from webscrape import TomatoeScrape, YoutubeScrape, DefinitionFind # import webscrape functions
import random
from flask import Flask, jsonify

app = Flask(__name__)

#####################
# File for commands #
#####################


#COMMANDS

@app.route("/")
def hello():
    return "Hello World!"

    # Marvin Webscrape Commands #

@app.route("/rottentomatoes/<movie>")
def rottentomatoes(movie):
    Tomatoe_Scrape = TomatoeScrape(movie)
    movie_data = Tomatoe_Scrape.scrapeRottentomatoes()
    return jsonify(movie_data)

@app.route("/imdbrating/<movie>")
def imdbrating(movie):
    Tomatoe_Scrape = TomatoeScrape(movie)
    movie_data = Tomatoe_Scrape.IMDb()
    return jsonify(movie_data)

@app.route("/youtube/<query>")
def youtube(query):
    Youtube_Scrape = YoutubeScrape(query)
    youtube_link = Youtube_Scrape.scrapeYoutube() # function to scrape urls
    return jsonify(youtube_link)

@app.route("/definition/<query>")
def define(query):
    Definition_Find = DefinitionFind(query)
    definition_data = Definition_Find.scrapeDefinition() # function to scrape urls
    return jsonify(definition_data)

    # Marvin Api Commands #
'''
    elif 'full random taco' == command:
        Api_Service = ApiService(speak_type)
        Api_Service.tacoFullRand()
        Api_Service.dataTaco()

    elif 'random taco' == command:
        Api_Service = ApiService(speak_type)
        Api_Service.tacoFullRand()
        Api_Service.dataTaco()
'''
if __name__ == '__main__':
   app.run(host='0.0.0.0', debug=False, threaded=True)
