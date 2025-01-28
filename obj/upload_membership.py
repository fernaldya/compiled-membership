from werkzeug.utils import secure_filename
from db import connect_pg, connect
from flask import request, jsonify


## Image
upload_dir = '/home/fernaldya/membership/images/'
allowed_ext = {'png', 'jpg', 'jpeg'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_ext

def save_to_db_pg(name, img_path, number):
