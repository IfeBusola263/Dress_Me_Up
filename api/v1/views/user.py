#!/usr/bin/python3
"""Creates all user route utility"""

from api.v1.views import app_views
from models.user import User
from flask import jsonify, request, render_template
from models import storage


@app_views.route('/users/sign_up',
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

@app_views.route('/users/login',
                 methods=["POST"],
                 strict_slashes=False)
def log_in(username=None, email=None, password=None):
    """Defines user login utility"""
    detail = request.get_json()
    print(detail)

    if not "name" in detail:
        return jsonify("Username cannot be empty"), 400

    if not "password" in detail:
        return jsonify("Password is required"), 400

    for value in storage.all(User).values():
        #print(value)
        dtl_name = detail["name"]

        val_name = value.make_json().get("name")
        dtl_pwd = detail["password"]
        val_pwd = value.make_json().get("password")
        detail_dict = {
                dtl_name: val_name,
                dtl_pwd: val_pwd
                }
        print(detail_dict)
        if detail["name"] == value.make_json().get("name") \
                and detail["password"] == value.make_json().get("password"):
                    return "<h1>Hello World!</h1>"
                    #return render_template("login.html")
    return jsonify("User not found")
