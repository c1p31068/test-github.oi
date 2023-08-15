from flask import Flask
from flask import render_template
from flask import Flask, request, render_template
import os


app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def hello_world():
    uploaded_files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('hello.html', uploaded_files=uploaded_files)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'ファイルがありません'

    file = request.files['file']

    if file.filename == '':
        return 'ファイルが選択されていません'

    if file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        return 'ファイルがアップロードされました'

@app.route('/delete/<filename>', methods=['GET'])
def delete_file(filename):
    try:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        os.remove(filepath)
        return 'ファイルが削除されました: {}'.format(filename)
    except Exception as e:
        return 'ファイルの削除に失敗しました: {}'.format(str(e))

if __name__ == '__main__':
    app.run(debug=True)
    