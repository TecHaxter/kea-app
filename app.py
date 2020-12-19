from flask import *  
app = Flask(__name__)  
import io
from cryptography.fernet import Fernet
import base64

@app.route('/')  
def upload():  
    return render_template("upload.html")  
 
@app.route('/decrypt', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        encrypted_file = request.files['file']
        key = request.form['key']
        decrypted_data = decrypt(encrypted_data=encrypted_file.read(), key=key)
        return send_file(io.BytesIO(decrypted_data), as_attachment=True,
                     attachment_filename=encrypted_file.filename,
                     mimetype=encrypted_file.mimetype)

def encrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)

def decrypt(encrypted_data, key):
    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_data)
    return decrypted_data

if __name__ == '__main__':  
    app.run(debug = True)  