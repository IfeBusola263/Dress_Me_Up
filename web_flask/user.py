#!/usr/bin/python3
"""Creates all user route utility"""
import os
from werkzeug.utils import secure_filename
from models.user import User
from flask import Flask, jsonify, request, render_template, send_from_directory, url_for, redirect, session
from models import storage
from models.event import Event
from models.dress import Dress
import hashlib

app = Flask(__name__)
app.secret_key = 'Jesusthesameyesterdaytoday'
UPLOAD_FOLDER = 'picture_uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'jpg', 'png', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=["GET", "POST"], strict_slashes=False)
def home():
    """A login route for users"""
    dresses = sorted(storage.all(Dress).values(), key=lambda d: d.name)
    if request.method == 'GET':
        return render_template('index.html', dresses=dresses)

    username = request.form.get('name')
    password = request.form.get('password')

    user = storage.get(User, username)
    if user and user.password == hashlib.md5(password.encode('utf-8')).hexdigest():
        return redirect(url_for('log_in', username=username))
    else:
        return jsonify("Invalid username or password")

@app.route('/users/login/<username>', methods=["GET", "POST"], strict_slashes=False)
def log_in(username):
    """Defines user login utility"""
    user = storage.get(User, username)
    if user:
        return render_template('user.html', username=username, profile_pic=user.profile_picture)
    else:
        return jsonify("User not found")
"""
@app.route('/', methods=["GET", "POST"], strict_slashes=False)
def home():
    A login route for users
    # events = sorted(storage.all(Event).values(), key=lambda e: e.name)
    dresses = sorted(storage.all(Dress).values(), key=lambda d: d.name)
    if request.method == 'GET':
        return render_template('index.html', dresses=dresses)

    username = request.form.get('name')
    password = request.form.get('password')

    user = storage.get(User, username)
    print("+++Here+++")
    if user and user.password == hashlib.md5(password.encode('utf-8')).hexdigest():
        print("+++Got Here+++")
        return redirect(url_for('log_in'))
    else:
        return jsonify("Invalid username or password")
"""

"""
@app.route('/users/login/<username>', methods=["GET", "POST"], strict_slashes=False)
def log_in(username, profile_pic=None):
    Defines user login utility
    username = request.form.get("name")
    user = storage.get(User, username)
    return render_template('user.html', username=username)

    if not user:
        return jsonify("User not found"), 404
    if request.method == 'GET':
        return render_template('user.html', username=username)

    username = request.form.get("name")
    user = storage.get(User, username)

    if not user:
        return jsonify("User not found"), 404

    passwd = request.form.get("password")
    passwd = hashlib.md5(passwd.encode('utf-8')).hexdigest()

    if passwd == user.password:
        print(username)
        print(user.profile_picture)
        return render_template("user.html", username=username, profile_pic=user.profile_picture)
    else:
        # Wrong password details
        return jsonify('Wrong Password, please try again')
"""

@app.route('/users/sign_up', methods=["POST", "GET"], strict_slashes=False)
def sign_up():
    """A login route for users"""
    if request.method == 'GET':
        return '''<form action="/users/sign_up" method="post" enctype="multipart/form-data">
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
            <input type="file" id="file" name="file"><br><br>

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
            return render_template('/profile.html', pp_url=pp_url)

@app.route('/collect_image')
def collect_image():
    """Uploads user image at signup"""
    return render_template('upload.html')

@app.route('/users/login',
           methods=["GET", "POST"],
           strict_slashes=False)
def login(username=None, email=None, password=None):
    """Defines user login utility"""
    if request.method == 'GET':
        return render_template('index.html')

    username = request.form.get("name")
    passwd  = request.form.get("password")
    passwd = hashlib.md5(passwd.encode('utf-8')).hexdigest()

    if not username:
        return jsonify("Username cannot be empty"), 400

    if not passwd:
        return jsonify("Password is required"), 400

    users = storage.all(User).values()
    for value in storage.all(User).values():
        if username == value.make_json().get("name"):
            username = value.make_json().get("name")
            profile_pic = value.make_json().get("profile_picture")
            if passwd == value.make_json().get("password"):
                return render_template("user.html", username=username, profile_pic=profile_pic)

            return jsonify('Wrong Password, you can try again')

    return jsonify("User not found")

@app.route('/users/sign_up', methods=["GET", "POST"], strict_slashes=False)
def sign_hup():
    """A route for user signup"""

    if request.method == 'GET':
        return render_template('signup.html')

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

        session['user_data'] = user_data
        return redirect(url_for('upload_profile_pic'))

@app.route('/users/upload_profile_pic', methods=["GET", "POST"])
def upload_profile_pic():
    """A route for uploading user profile picture"""

    if 'user_data' not in session:
        return redirect('/')

    if request.method == 'GET':
        return render_template('upload.html')

    if request.method == 'POST':
        try:
            file = request.files['file']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                upload_folder = app.config['UPLOAD_FOLDER']
                if not os.path.exists(upload_folder):
                    os.makedirs(upload_folder)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

                user_data = session.pop('user_data')
                user_data['profile_picture'] = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                new_user = User(**user_data)
                new_user.save()

                pp_url = url_for('uploaded_file', filename=filename)
                print(pp_url)
                return render_template('/profile.html', pp_url=pp_url)

            return jsonify("File upload failed or no file selected")
        except Exception as e:
            print(f"Error: {e}")

@app.route('/picture_uploads/<filename>')
def uploaded_file(filename):
    print(filename)
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == '__main__':
    app.run(port='5001', host='0.0.0.0', debug=True)
