# Imports
from marvin.rottentomatoes import TomatoeScrape
from marvin.define import DefinitionFind
from marvin.youtube import YoutubeScrape
from flask import Flask, jsonify

app = Flask(__name__)

'''
Server for Marvin Virtual Assistant to improve functionality
'''

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
