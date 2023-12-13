#!/usr/bin/python3
"""Creates all user route utility"""

from models.user import User
from flask import Flask, jsonify, request, render_template
from models import storage
import hashlib


app = Flask(__name__)

@app.route('/users/sign_up',
                 methods=["POST"],
                 strict_slashes=False)
def sign_up():
    """A login route for users"""
    detail = request.get_json()

    if "name" not in detail:
        return jsonify("name cannot be empty"), 400

    if not "password" in detail:
        return jsonify("password cannot be empty"), 400

    new_user = User(**detail)
    new_user.save()

    return jsonify("Peng! You have successfully registered"), 201


@app.route('/users/login',
                 methods=["GET", "POST"],
                 strict_slashes=False)
def log_in(username=None, email=None, password=None):
    """Defines user login utility"""
    # Serves the login form
    message = None

    # Serves the login form
    if request.method == 'GET':
        return render_template('index.html')

    # Get the username and password
    username = request.form.get("name")
    password = request.form.get("password")
    passwd = hashlib.md5(password.encode('utf-8')).hexdigest()

    # Validate username and password
    if not username:
        message = "Username cannot be empty"
        return render_template('index.html', message=message), 400

    if not password:
        message = "Password is required"
        return render_template('index.html', message=message), 400

    # Fetch user data from database
    for value in storage.all(User).values():

        # Confirm user name
        if username == value.make_json().get("name"):
            
            # Verify password with md5
            if passwd != value.make_json().get("password"):
                message = "Wrong password"
                return render_template('index.html', message=message), 401
        else:
            message = "User not found"

    return render_template('user.html', message=message)

if __name__ == '__main__':
    app.run(port='5001', host='0.0.0.0', debug=True)
