from flask import Flask, request, render_template, redirect, url_for, abort
import json
import os
import hashlib

app = Flask(__name__)

# Sample user data (replace this with your actual user data)
users = {
    0: {'name': 'John Doe', 'email': 'john@example.com', 'password': 'password123'},
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        form_data = request.form.to_dict(flat=True)
        hashed_password = hash_password(form_data['Password'])
        form_data['Password'] = hashed_password
        save_registration_details(user_id, form_data)
        return redirect(url_for('success'))
    else:
        return render_template('form.html', user_id=None)

@app.route('/form/<user_id>', methods=['GET', 'POST'])
def form(user_id):
    if request.method == 'POST':
        pass
    return render_template('form.html', user_id=user_id)

@app.route('/success', methods=['GET'])
def success():
    return render_template('success.html')

@app.route('/user/<user_id>', methods=['GET'])
def display_user(user_id):
    user_data = get_user_data(user_id)

    if user_data:
        return render_template('user_details.html', user=user_data)
    else:
        return render_template('user_not_found.html')

def get_user_data(user_id):
    return users.get(int(user_id), None)  # Convert user_id to integer for dictionary lookup


def save_registration_details(user_id, form_data):
    users[int(user_id)] = form_data

    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'users.txt')

    with open(file_path, 'w') as file:
        json.dump(users, file, indent=2)

def hash_password(password):
    password_bytes = password.encode('utf-8')

    sha256_hash = hashlib.sha256()

    sha256_hash.update(password_bytes)

    hashed_password = sha256_hash.hexdigest()

    return hashed_password

if __name__ == '__main__':
    app.run(host='localhost', port=5000)