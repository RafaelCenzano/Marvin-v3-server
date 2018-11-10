# Imports
from run import app
from flask import jsonify

# Routes
@app.route('/')
def index():
    return jsonify({'message': 'Hello, World!'})
