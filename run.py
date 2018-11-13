# Imports

# Flask imports
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

# Marvin Imports
import config

# Flask app
app = Flask(__name__)

# Configure app properties
app.config['SECRET_KEY'] = config.key
app.config['SQLALCHEMY_DATABASE_URI'] = config.database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create API property
api = Api(app)

# Create DB connection
db = SQLAlchemy(app)

# Import server modules
import views, models, resources

# Create tables
@app.before_first_request
def create_tables():
    db.create_all()

# Add routes
api.add_resource(resources.UserRegistration, '/registration')
api.add_resource(resources.UserLogin, '/login')
api.add_resource(resources.UserLogoutAccess, '/logout/access')
api.add_resource(resources.UserLogoutRefresh, '/logout/refresh')
api.add_resource(resources.TokenRefresh, '/token/refresh')
api.add_resource(resources.SecretResource, '/secret')
