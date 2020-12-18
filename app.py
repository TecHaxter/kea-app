from flask import *  
app = Flask(__name__)  
from encr import decrypt
import io

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
  
if __name__ == '__main__':  
    app.run(debug = True)  