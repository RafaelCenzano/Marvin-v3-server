# import database object
from run import db

# Import Hash
from passlib.hash import pbkdf2_sha256 as sha256

# Import config
import config

class UserModel(db.Model):
    # Create new user in table
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(120), unique = True, nullable = False)
    password = db.Column(db.String(120), nullable = False)

    # Add new user
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    # Check if user exists in database
    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username = username).first()

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password + config.SECURITY_PASSWORD_SALT)

    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password + config.SECURITY_PASSWORD_SALT, hash)
