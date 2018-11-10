from flask_restful import Resource, reqparse

# Parse incoming data
parser = reqparse.RequestParser()
parser.add_argument('username', help = 'This field cannot be blank', required = True)
parser.add_argument('password', help = 'This field cannot be blank', required = True)


class UserRegistration(Resource):
    def post(self):
        data = parser.parse_args()
        new_user = UserModel(
            username = data['username'],
            password = data['password']
        )
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
        return {'message': 'User login'}


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


class AllUsers(Resource):
    def get(self):
        data = parser.parse_args()
        return {'message': 'List of users'}

    def delete(self):
        data = parser.parse_args()
        return {'message': 'Delete all users'}


class SecretResource(Resource):
    def get(self):
        data = parser.parse_args()
        return {
            'answer': 42
        }
