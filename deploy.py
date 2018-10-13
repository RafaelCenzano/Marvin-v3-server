# Imports
from api import ApiService # classes to handle api work
from webscrape import TomatoeScrape, YoutubeScrape, DefinitionFind # import webscrape functions
from flask import Flask, jsonify

app = Flask(__name__)
app.add_url_rule('/favicon.ico',
                 redirect_to=url_for('static', filename='favicon.ico'))

#####################
# File for commands #
#####################


#COMMANDS

@app.route("/")
def hello():
    return "<h1>Hello World! Welcome to Marvin api service</h1>"

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
