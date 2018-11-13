from run import db

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
