#!/usr/bin/python3
"""Creates all user route utility"""
import os
from werkzeug.utils import secure_filename
from models.user import User
from flask import Flask, jsonify, request, render_template, send_from_directory, url_for, redirect
from models import storage
import hashlib

app = Flask(__name__)

UPLOAD_FOLDER = 'picture_uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'jpg', 'png', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/users/sign_up', methods=["POST", "GET"], strict_slashes=False)
def sign_up():
    """A login route for users"""
    if request.method == 'GET':
        return '''
          <form action="/users/sign_up" method="post" enctype="multipart/form-data">
            <label for="name">Username:</label>
            <input type="text" id="name" name="name"><br><br>

            <label for="email">Email:</label>
            <input type="email" id="email" name="email"><br><br>

            <label for="measurement">Measurement:</label>
            <input type="text" id="measurement" name="measurement"><br><br>

            <label for="outfits">Outfits:</label>
            <input type="text" id="outfits" name="outfits"><br><br>

            <label for="country">Country:</label>
            <input type="text" id="country" name="country"><br><br>

            <label for="state">State:</label>
            <input type="text" id="state" name="state"><br><br>

            <label for="password">Password:</label>
            <input type="password" id="password" name="password"><br><br>

            <label for="file">Profile Picture:</label>
            <input type="file" id="file" name="file">
            <button type="upload" id="upload" name="upload">upload</button><br><br>

            <input type="submit" value="Submit">
          </form>
        '''
    if request.method == 'POST':
        user_data = {
            "name": request.form.get("name"),
            "email": request.form.get("email"),
            "measurement": request.form.get("measurement"),
            "outfits": request.form.get("outfits"),
            "country": request.form.get("country"),
            "state": request.form.get("state"),
            "password": request.form.get("password")
        }


        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            upload_folder = app.config['UPLOAD_FOLDER']
            if not os.path.exists(upload_folder):
                os.makedirs(upload_folder)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            user_data['profile_picture'] = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            new_user = User(**user_data)
            new_user.save()
            pp_url = url_for('uploaded_file', filename=filename)
            print(pp_url)
            # return redirect(url_for('uploaded_file', filename=filename))
            return render_template('/profile.html', pp_url=pp_url)
        """else:
            user_data['profile_picture'] = None

        new_user = User(**user_data)
        new_user.save()

        if user_data.get('profile_picture'):
            profile_picture_url = url_for('uploaded_file', filename=user_data['profile_picture'], _external=True)
        else:
            profile_picture_url = None
        print(profile_picture_url)
        return render_template('profile.html', profile_picture_url=profile_picture_url)"""


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

@app.route('/picture_uploads/<filename>')
def uploaded_file(filename):
    print(filename)
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == '__main__':
    app.run(port='5001', host='0.0.0.0', debug=True)
