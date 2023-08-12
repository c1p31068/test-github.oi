from flask import Flask, request, render_template
import os

app = Flask(__name__)

# アップロードされたファイルを保存するディレクトリ
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

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

if __name__ == '__main__':
    app.run(debug=True)
