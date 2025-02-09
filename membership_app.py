import os
from flask import Flask, render_template, request, jsonify, make_response
from dotenv import load_dotenv
from obj.db import connect_pg
from obj.insert import insert_data_pg, add_owner_pg, MembershipExistsError
from obj.delete import delete_membership_pg, delete_owner_pg


load_dotenv()

membership_app = Flask(__name__, static_folder='static')
membership_app.config['UPLOAD_DIR'] = os.path.join('static', 'img')

if not os.path.exists(membership_app.config['UPLOAD_DIR']):
    os.makedirs(membership_app.config['UPLOAD_DIR'])

# def no_cache(response):
#     response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
#     response.headers['Pragma'] = 'no-cache'
#     response.headers['Expires'] = '-1'
#     return response


@membership_app.route("/")
def home():
    """Render index.html"""
    conn = connect_pg()
    try:
        with conn.cursor() as cursor:
            sql_member = 'select name, membership_number, membership_uri, owner from memberships'
            cursor.execute(sql_member)
            memberships = cursor.fetchall()
            memberships = [{'name': row[0], 'number': row[1], 'image': row[2], 'owner': row[3]} for row in memberships]

            sql_owner = 'select distinct owner from owners'
            cursor.execute(sql_owner)
            owners = cursor.fetchall()
            owners = [{'owner': row[0]} for row in owners]
    finally:
        conn.close()

    return render_template('index.html', memberships=memberships, owners=owners)


@membership_app.route("/upload", methods=['POST'])
def fetch_user_upload():
    name = request.form.get('membership_name').upper().strip()
    img = request.files.get('file')
    number = request.form.get('number').strip()
    owner = request.form.get('owner')

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
        insert_data_pg(name, file_path, membership_number, owner)
    except MembershipExistsError as e:
        return jsonify({'error': str(e)}), 400

    return jsonify({
        'message': 'Membership uploaded successfully!',
        'name': name,
        'path': file_path,
        'number': number
    }), 200

@membership_app.route("/delete", methods=['DELETE'])
def delete_membership():
    data = request.get_json()
    name = data.get('name')
    if not name:
        return jsonify({'error': 'Membership name is required!'}), 400
    try:
        result = delete_membership_pg(name)
        if result == 'Membership not found!':
            return jsonify({'error': result}), 404
        else:
            return jsonify({'message': result}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


# Ownership
@membership_app.route("/ownership", methods=['GET'])
def ownership():
    conn = connect_pg()
    try:
        with conn.cursor() as cursor:
            sql = 'select owner from owners'
            cursor.execute(sql)
            owners = cursor.fetchall()
            owners = [{'owner': row[0]} for row in owners]
    finally:
        conn.close()

    return render_template('ownership.html', owners=owners)

@membership_app.route("/add_owner", methods=['POST'])
def add_owner():
    owner_name = request.form.get('owner_name').upper().strip()

    if not owner_name:
        return jsonify({'error': 'Owner name is required!'}), 400

    try:
        add_owner_pg(owner_name)
        return jsonify({'message': 'Owner added successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@membership_app.route("/delete_owner", methods=['DELETE'])
def delete_owner():
    data = request.get_json()
    owner_name = data.get('owner')
    if not owner_name:
        return jsonify({'error': 'Owner name is required!'}), 400
    try:
        result = delete_owner_pg(owner_name)
        return jsonify({'message': result}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    membership_app.run(debug=True, port=5000)
