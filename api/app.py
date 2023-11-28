#!/usr/bin/python3
"""Sets up the app"""

from api.v1.views import app_views
from models import storage
from flask import Flask, jsonify
from flask_cors import CORS
import os


app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/api/v1/*": {"origin": "*"}})

@app.teardown_appcontext
def tear_down(error):
    """defines a teardown method for closing storage"""
    storage.close()

@app.errorhandler(404)
def error_handling(err):
    """Handle 404 Not found"""
    return jsonify({"error": "Not found"}), 404


if __name__ == '__main__':
    PORT = os.getenv("DRESS_ME_API_PORT")
    HOST = os.getenv("DRESS_ME_API_HOST")
    if not HOST:
        HOST = '0.0.0.0'
    if not PORT:
        PORT = '5000'

    app.run(host=HOST,
            port=PORT,
            threaded=True)
