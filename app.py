#!/usr/bin/env python3
from cryptography.fernet import Fernet
import os.path
import io
from flask import *

app = Flask(__name__)

@app.route('/')
def upload():
    # with open('filekey.key', 'rb') as filekey:
    #     key = filekey.read()
    # return render_template("upload.html", key=key)
    return render_template("upload.html")


@app.route('/decrypt', methods=['POST'])
def decryptRequest():
    if request.method == 'POST':
        encrypted_file = request.files['file']
        key = request.form['key']
        decrypted_data = decrypt(encrypted_data=encrypted_file.read(), key=key)
        return send_file(io.BytesIO(decrypted_data), as_attachment=True,
                         attachment_filename=encrypted_file.filename,
                         mimetype=encrypted_file.mimetype)


@app.route('/encrypt', methods=['POST'])
def encryptRequest():
    if request.method == 'POST':
        original_file = request.files['file']
        encrypted_data, encrypt_key = encrypt(
            original_data=original_file.read(),
            )

        print(encrypt_key) 
        with open(f'{original_file.filename}.key', 'wb') as filekey:
            filekey.write(encrypt_key)   

        return send_file(io.BytesIO(encrypted_data), as_attachment=True,
                         attachment_filename=original_file.filename,
                         mimetype=original_file.mimetype)


def encrypt(original_data):
    key = Fernet.generate_key()

    f = Fernet(key)
    encrypted_data = f.encrypt(original_data)
    # print(key)
    return encrypted_data, key


def decrypt(encrypted_data, key):
    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_data)
    return decrypted_data


if __name__ == '__main__':
    app.run(debug=True)
