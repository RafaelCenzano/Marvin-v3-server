# Imports

# Marvin code imports
from marvin.rottentomatoes import TomatoeScrape
from marvin.define import DefinitionFind
from marvin.youtube import YoutubeScrape
#from marvin.database import db_session, init_db
from marvin.models import User, Role, Base
import config

# Flask and extensions imports
from flask import Flask, jsonify, request, render_template # Flask module
from flask_sqlalchemy import SQLAlchemy # SQLAlchemy for database work
from flask_security import Security, SQLAlchemySessionUserDatastore, auth_token_required # Security modules

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = config.key

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

# Create a user to test with
@app.before_first_request
def create_user():
    db.create_all()
    if not User.query.first():
        user_datastore.create_user(email='test@example.com', password='test123')
        db.session.commit()

'''
Server for Marvin Virtual Assistant to improve functionality
'''

# TEST ROUTE
@app.route('/dummy-api/', methods=['GET'])
@auth_token_required
def dummyAPI():
    ret_dict = {
        "Key1": "Value1",
        "Key2": "value2"
    }
    return jsonify(items=ret_dict)

# ROUTES

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
@auth_token_required
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
