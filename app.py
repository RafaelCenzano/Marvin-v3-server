# Imports

# Marvin code imports
from marvin.rottentomatoes import TomatoeScrape
from marvin.define import DefinitionFind
from marvin.youtube import YoutubeScrape
from marvin.database import db_session, init_db
from marvin.models import User, Role
import config

# Flask and extensions imports
from flask import Flask, jsonify, request, render_template # Flask module
from flask_sqlalchemy import SQLAlchemy # SQLAlchemy for database work
from flask_heroku import Heroku # Heroku configuration
from flask_security import Security, login_required, SQLAlchemySessionUserDatastore # Security modules


app = Flask(__name__)
app.config['DEBUG'] = True
init_db()
app.config['SECRET_KEY'] = config.key
#heroku = Heroku(app) # for heroku
#db = SQLAlchemy(app)

# Setup Flask-Security
user_datastore = SQLAlchemySessionUserDatastore(db_session, User, Role)
security = Security(app, user_datastore)

# Create a user to test with
#@app.before_first_request
def create_user():
    init_db()
    user_datastore.create_user(email='matt@nobien.net', password='password')
    db_session.commit()

'''
Server for Marvin Virtual Assistant to improve functionality
'''

# COMMANDS

@app.errorhandler(404)
def page_not_found():
    return jsonify({'code':404}) # redirect to /404_not_found

@app.errorhandler(400)
def page_not_found():
    return jsonify({'code':400}) # redirect to /404_not_found

@app.errorhandler(500)
def page_not_found():
    return jsonify({'code':500}) # redirect to /404_not_found

@app.route("/", methods=['GET'])
def hello():
    return jsonify({'home':'Welcome to the home of the marvin api'})

    # Marvin Webscrape Commands #

@app.route("/api/v1/rottentomatoes/<movie>")
@login_required
def rottentomatoes(movie):
    Tomatoe_Scrape = TomatoeScrape(movie)
    movie_data = Tomatoe_Scrape.scrapeRottentomatoes()
    if movie_data == 400:
        return 400
    return jsonify(movie_data)

@app.route("/api/v1/imdbrating/<movie>", methods=['GET'])
def imdbrating(movie):
    Tomatoe_Scrape = TomatoeScrape(movie)
    movie_data = Tomatoe_Scrape.IMDb()
    if movie_data == 400:
        return 400
    return jsonify(movie_data)

@app.route("/api/v1/youtube/<query>", methods=['GET'])
def youtube(query):
    Youtube_Scrape = YoutubeScrape(query)
    youtube_link = Youtube_Scrape.scrapeYoutube() # function to scrape urls
    return jsonify(youtube_link)

@app.route("/api/v1/definition/<query>", methods=['GET'])
def define(query):
    Definition_Find = DefinitionFind(query)
    definition_data = Definition_Find.scrapeDefinition() # function to scrape urls
    if definition_data == 400:
        return 400
    return jsonify(definition_data)
