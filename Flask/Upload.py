from flask import Flask, request, jsonify, send_file
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'files' not in request.files:
        return jsonify({'error': 'No file part'})

    files = request.files.getlist('files')

    for file in files:
        file.save(os.path.join(UPLOAD_FOLDER, file.filename))

    return jsonify({'message': 'Files uploaded successfully'})

@app.route('/request', methods=['GET'])
def request_file():
    files = os.listdir(UPLOAD_FOLDER)
    if len(files) == 0:
        return jsonify({'error': 'No files available'})

    # For simplicity, just return the first file found
    requested_file = files[0]

    # Provide the requested file for download
    return send_file(os.path.join(UPLOAD_FOLDER, requested_file), as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
