from flask import Flask,send_file
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def hello():
    return 'Hello!'

@app.route("/img/<string:file_name>", methods=["GET"])
def get_img(file_name):
    filepath = "./" + file_name
    filename = os.path.basename(filepath)
    return send_file(filepath, as_attachment=True,
                     attachment_filename=filename,
                     mimetype='img/png')

if __name__ == "__main__":
    # app.run(host='192.168.0.119', port=3000)
    app.run(port=8080)