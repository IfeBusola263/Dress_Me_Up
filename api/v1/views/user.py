#!/usr/bin/python3
"""Creates all user route utility"""

from api.v1.views import app_views
from models.user import User
from flask import jsonify, request, render_template
from models import storage
import hashlib


@app_views.route('/users/sign_up',
                 methods=["POST"],
                 strict_slashes=False)
def sign_up():
    """A login route for users"""
    detail = request.get_json()

    if "name" not in detail:
        return jsonify("name cannot be empty"), 400

    if "password" not in detail:
        return jsonify("password cannot be empty"), 400

    new_user = User(**detail)
    new_user.save()

    return jsonify("Peng! You have successfully registered"), 201


@app_views.route('/users/login',
                 methods=["POST"],
                 strict_slashes=False)
def log_in(username=None, email=None, password=None):
    """Defines user login utility"""
    detail = request.get_json()

    if "name" not in detail:
        return jsonify("Username cannot be empty"), 400

    if "password" not in detail:
        return jsonify("Password is required"), 400

    for value in storage.all(User).values():

        # Confirm user name
        if detail["name"] == value.make_json().get("name"):

            # Verify Password
            passwd = hashlib.md5(detail['password'].encode('utf-8'))
            passwd = passwd.hexdigest()
            if passwd == value.make_json().get("password"):
                # return "<h1>Hello World!</h1>"
                return render_template("login.html", name=detail['name'])

            # Wrong password details
            return jsonify('Wrong Password, you can try again')

    # User not found in the database
    return jsonify("User not found")
