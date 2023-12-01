from models import storage
from models.dress import Dress
from models.event import Event
from flask import Flask, render_template, send_from_directory, request, redirect, url_for
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# UPLOADED_FOLDER = '~/Dress_Me_Up/web_flask/dress_images'
UPLOADED_FOLDER = os.getcwd() + '/web_flask/dress_images'
print(UPLOADED_FOLDER)
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'webp', 'gif'}
app.config['UPLOADED_FOLDER'] = UPLOADED_FOLDER

def allowed_file(filename):
    """Validates allowed file"""
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.teardown_appcontext
def tearDown(exception):
    """Defines a teardown method for closing the database"""
    storage.close()

@app.route('/dress_me', methods=["GET"])
def dress_display():
    """Displays all dresses of different kinds"""
    dresses = sorted(storage.all(Dress).values(), key=lambda d: d.name)
    events = storage.all(Event).values()
    events = [ event.make_json() for event in events ]
    return render_template('dresses.html', dresses=dresses, events=events)

@app.route('/re_update_dress/<name>', methods=["GET", "POST"])
def recreate_dress(name):
    """Updates dress database"""
    dress = storage.get(Dress, name)
    print(dress)
    if not dress:
        return "Dress not found"
    
    if request.method == 'GET':
        if dress.image == 'No Image':
            return render_template('dress_upload.html', dress_name=name)
    print("================Got here=======================")

    file = request.files['file']
    print("================and here=======================")
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOADED_FOLDER'], filename)
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print(os.path.dirname(file_path))
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        file.save(file_path)
        dress.image = file_path
        storage.save()

    return redirect(url_for('uploaded_dress', filename=filename))

@app.route("/upload_dress/<path:filename>")
def uploaded_dress(filename):
    """Display uploaded dress image"""
    print("=====Here we are=========")
    result = send_from_directory(app.config['UPLOADED_FOLDER'], filename)
    print(result)
    return result 


if __name__ == '__main__':
    app.run(port='5000', host='0.0.0.0', debug=True)

