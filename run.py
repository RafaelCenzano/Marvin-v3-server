# Imports

# Flask imports
from flask import Flask
from flask_restful import Api

# Flask app
app = Flask(__name__)

# Create API
api = Api(app)

# Import server modules
import views, models, resources

# Add routes
api.add_resource(resources.UserRegistration, '/registration')
api.add_resource(resources.UserLogin, '/login')
api.add_resource(resources.UserLogoutAccess, '/logout/access')
api.add_resource(resources.UserLogoutRefresh, '/logout/refresh')
api.add_resource(resources.TokenRefresh, '/token/refresh')
api.add_resource(resources.AllUsers, '/users')
api.add_resource(resources.SecretResource, '/secret')
