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
    if request.method == 'GET':
        return render_template('index.html')

    # Get the username and hash the password
    username = request.form.get("name")
    passwd  = request.form.get("password")
    passwd = hashlib.md5(passwd.encode('utf-8')).hexdigest()

    if not username:
        return jsonify("Username cannot be empty"), 400

    if not passwd:
        return jsonify("Password is required"), 400

    for value in storage.all(User).values():

        # Confirm user name
        if username == value.make_json().get("name"):

            # Verify Password
            # passwd = hashlib.md5(detail['password'].encode('utf-8'))
            # passwd = passwd.hexdigest()
            if passwd == value.make_json().get("password"):
                # return "<h1>Hello World!</h1>"
                return render_template("login.html", name=username)

            # Wrong password details
            return jsonify('Wrong Password, you can try again')

    # User not found in the database
    return jsonify("User not found")


if __name__ == '__main__':
    app.run(port='5001', host='0.0.0.0', debug=True)
