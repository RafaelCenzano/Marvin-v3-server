# Imports
from run import app
from flask import jsonify

# Home Route / Testing
@app.route('/')
def index():
    return jsonify({'message': 'Hello, World!'})
