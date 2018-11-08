# Imports

# Marvin code imports
from marvin.rottentomatoes import TomatoeScrape
from marvin.define import DefinitionFind
from marvin.youtube import YoutubeScrape
#from marvin.database import Base
#from marvin.models import User, Role
import config

# Flask and extensions imports
from flask import Flask, jsonify, request, render_template # Flask module
from flask_sqlalchemy import SQLAlchemy # SQLAlchemy for database work
from flask_security import Security, SQLAlchemyUserDatastore, auth_token_required # Security modules

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = config.key
app.config['SQLALCHEMY_DATABASE_URI'] = config.database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['WTF_CSRF_ENABLED'] = False
app.config['SECURITY_PASSWORD_HASH'] config.SECURITY_PASSWORD_HASH
app.config['SECURITY_TRACKABLE'] = config.SECURITY_TRACKABLE
app.config['SECURITY_PASSWORD_SALT'] = config.SECURITY_PASSWORD_SALT
db = SQLAlchemy(app)

class Base(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified_at = db.Column(db.DateTime, default=db.func.current_timestamp(),
                            onupdate=db.func.current_timestamp())

roles_users = db.Table('roles_users',
                       db.Column('user_id', db.Integer(),
                                 db.ForeignKey('auth_user.id')),
                       db.Column('role_id', db.Integer(),
                                 db.ForeignKey('auth_role.id')))


from flask_security import UserMixin, RoleMixin
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Boolean, DateTime, Column, Integer, String

class Role(Base, RoleMixin):
    __tablename__ = 'auth_role'
    name = db.Column(db.String(80), nullable=False, unique=True)
    description = db.Column(db.String(255))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Role %r>' % self.name

class User(Base, UserMixin):
    __tablename__ = 'auth_user'
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(45))
    current_login_ip = db.Column(db.String(45))
    login_count = db.Column(db.Integer)
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

    def __repr__(self):
        return '<User %r>' % self.email


# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)


'''
# Create a user to test
@app.before_first_request
def create_user():
    db.create_all()
    if not User.query.first():
        user_datastore.create_user(email='test@example.com', password='test123')
        db.session.commit()
'''


'''
Server for Marvin Virtual Assistant to improve functionality
This server uses flask, flask-security, and sqlalchemy to create a safe API
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
    return jsonify({'code':404}) # return error code

@app.errorhandler(400)
def page_not_found():
    return jsonify({'code':400}) # return error code

@app.errorhandler(500)
def page_not_found():
    return jsonify({'code':500}) # return error code

@app.route("/", methods=['GET'])
def hello():
    return jsonify({'home':'Welcome to the home of the marvin api'})

    # Marvin Webscrape Commands #

# Route that contains code to allow for rotten tomatoes data about search query
@app.route("/api/v1/rottentomatoes/<movie>")
def rottentomatoes(movie):
    Tomatoe_Scrape = TomatoeScrape(movie)
    movie_data = Tomatoe_Scrape.scrapeRottentomatoes()
    if movie_data == 400:
        return 400
    return jsonify(movie_data)

# Route that contains code to allow for imdb data about search query
@app.route("/api/v1/imdbrating/<movie>", methods=['GET'])
def imdbrating(movie):
    Tomatoe_Scrape = TomatoeScrape(movie)
    movie_data = Tomatoe_Scrape.IMDb()
    if movie_data == 400:
        return 400
    return jsonify(movie_data)

# Route that contains code to allow for youtube links for search query
@app.route("/api/v1/youtube/<query>", methods=['GET'])
def youtube(query):
    Youtube_Scrape = YoutubeScrape(query)
    youtube_link = Youtube_Scrape.scrapeYoutube() # function to scrape urls
    return jsonify(youtube_link)

# Route that contains code to allow for definition information
@app.route("/api/v1/definition/<query>", methods=['GET'])
def define(query):
    Definition_Find = DefinitionFind(query)
    definition_data = Definition_Find.scrapeDefinition() # function to scrape urls
    if definition_data == 400:
        return 400
    return jsonify(definition_data)
