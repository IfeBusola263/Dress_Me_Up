#!/usr/bin/python3
"""Creates all user route utility"""

from models.user import User
from flask import Flask, jsonify, request, render_template
from models import storage

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

@app.route('/users/login', methods=["GET", "POST"], strict_slashes=False)
def log_in():
    """Defines user login utility"""
    if request.method == "GET":
        return render_template("index.html")

    username = request.form.get("name")
    password = request.form.get("password")

    if not username:
        return jsonify("Username cannot be empty"), 400

    if not password:
        return jsonify("Password is required"), 400

    for value in storage.all(User).values():
        val_name = value.make_json().get("name")
        val_pwd = value.make_json().get("password")

        if username == val_name and password == val_pwd:
            return render_template("login.html")

    return jsonify("User not found")


if __name__ == '__main__':
    app.run(port='5001', host='0.0.0.0', debug=True)
