# Imports

# Flask imports
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

# Marvin Imports
import config

# Flask app
app = Flask(__name__)

# Configure app properties
app.config['SECRET_KEY'] = config.KEY
app.config['SQLALCHEMY_DATABASE_URI'] = config.DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.MOD
app.config['JWT_SECRET_KEY'] = config.JWT_SECRET_KEY
app.config['JWT_BLACKLIST_ENABLED'] = config.BLACKLIST
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = config.TOKEN

# Create API property
api = Api(app)

# Create DB connection
db = SQLAlchemy(app)

# Create JWT manager
jwt = JWTManager(app)

# Import server modules
import views, models, resources

# Create JWT blacklist
@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return models.RevokedTokenModel.is_jti_blacklisted(jti)

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
api.add_resource(resources.SecretResource, '/hidden')
api.add_resource(resources.Test, '/test/<test_var>')
api.add_resource(resources.RottenTomatoes, '/api/v1/rottentomatoes/<movie>')
api.add_resource(resources.RottenTomatoesIMDb, '/api/v1/imdbrating/<movie>')
