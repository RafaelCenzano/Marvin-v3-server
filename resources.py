# Flask Imports
from flask_restful import Resource, reqparse

# Model Imports
from models import UserModel

# Parse incoming data
parser = reqparse.RequestParser()
parser.add_argument('username', help = 'This field cannot be blank', required = True)
parser.add_argument('password', help = 'This field cannot be blank', required = True)


class UserRegistration(Resource):
    def post(self):
        # Parse data sent
        data = parser.parse_args()

        # Check if user exists
        if UserModel.find_by_username(data['username']):
            return {'message': 'User {} already exists'. format(data['username'])}

        # Get data to make new user
        new_user = UserModel(
            username = data['username'],
            password = data['password']
        )

        # Create user in db
        try:
            new_user.save_to_db()
            return {
                'message': 'User {} was created'.format( data['username'])
            }
        except:
            return {'message': 'Something went wrong'}, 500


class UserLogin(Resource):
    def post(self):
        data = parser.parse_args()
        current_user = UserModel.find_by_username(data['username'])
        if not current_user:
            return {'message': 'User {} doesn\'t exist'.format(data['username'])}

        if data['password'] == current_user.password:
            return {'message': 'Logged in as {}'.format(current_user.username)}
        else:
            return {'message': 'Wrong credentials'}


class UserLogoutAccess(Resource):
    def post(self):
        data = parser.parse_args()
        return {'message': 'User logout'}


class UserLogoutRefresh(Resource):
    def post(self):
        data = parser.parse_args()
        return {'message': 'User logout'}


class TokenRefresh(Resource):
    def post(self):
        data = parser.parse_args()
        return {'message': 'Token refresh'}


class SecretResource(Resource):
    def get(self):
        data = parser.parse_args()
        return {
            'answer': 42
        }
