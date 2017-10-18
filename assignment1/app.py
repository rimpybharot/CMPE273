from flask import Flask, request
import os
import json
import rocksdb, uuid
import subprocess

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'app/v1/scripts/')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/app/v1/scripts/<scriptid>', methods=['GET'])
def get(scriptid):
    db = rocksdb.DB("assignment1.db", rocksdb.Options(create_if_missing=True))
    filename = db.get((scriptid.encode())).decode()
    resp = subprocess.check_output(['python3.6', str(os.path.join(UPLOAD_FOLDER, filename))])
    return resp, 200

@app.route('/app/v1/scripts/', methods=['POST'])
def post():
    db = rocksdb.DB("assignment1.db", rocksdb.Options(create_if_missing=True))
    file = request.files.get("data")
    file.save(os.path.join(UPLOAD_FOLDER, file.filename))
    key = uuid.uuid4().hex
    db.put(key.encode(), (str(file.filename)).encode());
    resp = json.dumps({'script-id':key})
    return resp, 201


if __name__ == '__main__':
    app.run(debug=True, port=8000)
