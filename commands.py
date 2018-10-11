#Imports
from os import system, path # run terminal commands and find files in path
from json import load, dump # import json load
from difflib import get_close_matches # import close matches functions
from datetime import datetime # import datetime to show date and time
from threading import Thread # import threading to run more than one job at a time
from marvin.api import ApiService # classes to handle api work
from marvin.webscrape import TomatoeScrape, YoutubeScrape, DefinitionFind # import webscrape functions
import random
from flask import Flask, jsonify

app = Flask(__name__)

#####################
# File for commands #
#####################


command_list = ['open reddit', 'open subreddit', 'define', 'what is the definition of','google','where is','amazon','open google docs','open google sheets',
                    'time in','rotten tomatoes','imdb','imdb rating','youtube','search youtube','standby','exit','quit','leave','close','relog','logout','ls',
                    'dir','contacts','contact list','remove contact','delete contact','add contact','new contact','send email','roll a die','shut down','shutdown'
                    'what time is it','current time','what is the date','what\'s the date','current date','date today','d6','6 sided die','set a timer for'
                    'day of the week','week number','open calculator','run calculator','calculator','open stopwatch','run stopwatch','stopwatch','roll a d6',
                    'roll a 6 sided die','dice','what dice can I roll','flip coin','flip a coin','open twitter','open facebook','open github'
                ]


#COMMANDS

@app.route("/")
def hello():
    return "Hello World!"

    # Marvin Webscrape Commands #

@app.route("/rottentomatoes/<movie>")
def rottentomatoes(movie):
    TomatoeScrape = TomatoeScrape(movie)
    movie_data = TomatoeScrape.scrapeRottentomatoes()
    return jsonify(movie_data)

    elif 'imdb' in command:
        if 'imdb rating' in command:
            num_type = 2
        elif 'imdb' in command:
            num_type = 1
        TomatoeScrape = TomatoeScrape(speak_type, command, num_type)
        TomatoeScrape.IMDb()

    elif 'youtube' in command:
        if 'search youtube' in command:
            num_type = 2
        elif 'play in youtube' in commands:
            num_type = 3
        elif 'youtube' in command:
            num_type = 1
        Youtube_Scrape = YoutubeScrape(speak_type, command, num_type)
        Youtube_Scrape.scrapeYoutube() # function to scrape urls

    elif 'define' in command or 'what is the definition of' in command:
        if 'what is the definition of' in command:
            num_type = 5
        elif 'define' in command:
            num_type = 1
        Definition_Find = DefinitionFind(speak_type, command, num_type)
        Definition_Find.scrapeDefinition() # function to scrape urls

    # Marvin Api Commands #

    elif 'full random taco' == command:
        Api_Service = ApiService(speak_type)
        Api_Service.tacoFullRand()
        Api_Service.dataTaco()

    elif 'random taco' == command:
        Api_Service = ApiService(speak_type)
        Api_Service.tacoFullRand()
        Api_Service.dataTaco()
