import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from obj.insert_db import insert_data_pg, MembershipExistsError


load_dotenv()

membership_app = Flask(__name__)
membership_app.config['UPLOAD_DIR'] = os.getenv('IMG_LOCAL_DIR')

@membership_app.route("/")
def home():
    """Render index.html"""
    return render_template('index.html')


@membership_app.route("/upload", methods=['POST'])
def fetch_user_upload():
    name = request.form.get('membership_name').upper()
    img = request.files.get('file')
    number = request.form.get('number').upper()

    if not name:
        return '<h1>Membership name is required.</h1>', 400

    if not img and not number:
        return '<h1>Either an iamge or the membership number is required.</h1>', 400

    if img and img.filename == '':
        return '<h1>No file selected.</h1>', 400

    file_path = None
    if img:
        ext = '.' + img.filename.rsplit('.')[-1]
        filename = name + ext
        file_path = os.path.join(membership_app.config['UPLOAD_DIR'], filename)
        img.save(file_path)

    membership_number = None
    if number:
        membership_number = number

    try:
        insert_data_pg(name, file_path, membership_number)
    except MembershipExistsError as e:
        return jsonify({'error': str(e)}), 400

    return jsonify({
        'message': 'Membership uploaded successfully!',
        'name': name,
        'path': file_path,
        'number': number
    }), 200

if __name__ == '__main__':
    membership_app.run(debug=True)
