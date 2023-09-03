from flask import Flask
from flask import render_template
from flask import Flask, request, render_template
import os
import sqlite3

# データベースの初期化とテーブルの作成
conn = sqlite3.connect('comments.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS comments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content TEXT
)
''')

conn.commit()
conn.close()



app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def index():
    conn = sqlite3.connect('comments.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM comments')
    comments = cursor.fetchall()

    conn.close()

    return render_template('chiha.html', comments=comments)
   


@app.route('/post_comment', methods=['POST'])
def post_comment():
    content = request.form.get('comment_content')
    if content:
        conn = sqlite3.connect('comments.db')
        cursor = conn.cursor()

        cursor.execute('INSERT INTO comments (content) VALUES (?)', (content,))
        conn.commit()

        conn.close()


    return render_template("view_comments.html")

@app.route('/view_comments')
def view_comments():
    conn = sqlite3.connect('comments.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM comments')
    comments = cursor.fetchall()

    conn.close()

    return render_template('view_comments.html', comments=comments)


@app.route("/hello", methods=["GET"]) 
def hello_world():
    uploaded_files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('hello.html', uploaded_files=uploaded_files)

    

@app.route("/bronze", methods=["GET"]) 
def chinu_file():
    uploaded_files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('chinu.html', uploaded_files=uploaded_files)


    
    from flask import Flask, request, render_template
import os
import sqlite3

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# データベースの初期化とテーブルの作成
conn = sqlite3.connect('comments.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS comments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content TEXT
)
''')

conn.commit()
conn.close()

@app.route("/")
def index():
    conn = sqlite3.connect('comments.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM comments')
    comments = cursor.fetchall()

    conn.close()

    return render_template('chiha.html', comments=comments)

@app.route('/post_comment', methods=['POST'])
def post_comment():
    content = request.form.get('comment_content')
    if content:
        conn = sqlite3.connect('comments.db')
        cursor = conn.cursor()

        cursor.execute('INSERT INTO comments (content) VALUES (?)', (content,))
        conn.commit()

        conn.close()

    return render_template("view_comments.html")

@app.route('/view_comments')
def view_comments():
    conn = sqlite3.connect('comments.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM comments')
    comments = cursor.fetchall()

    conn.close()

    return render_template('view_comments.html', comments=comments)

@app.route("/hello", methods=["GET"]) 
def hello_world():
    uploaded_files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('hello.html', uploaded_files=uploaded_files)

@app.route("/bronze", methods=["GET"]) 
def chimu():
    uploaded_files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('chinu.html', uploaded_files=uploaded_files)

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




@app.route('/upload1', methods=['POST'])
def upload_file1():
    if 'file' not in request.files:
        return 'ファイルがありません'

    file = request.files['file']

    if file.filename == '':
        return 'ファイルが選択されていません'

    if file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        return 'ファイルがアップロードされました'

@app.route('/delete1/<filename>', methods=['GET'])
def delete_file1(filename):
    try:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        os.remove(filepath)
        return 'ファイルが削除されました: {}'.format(filename)
    except Exception as e:
        return 'ファイルの削除に失敗しました: {}'.format(str(e))

if __name__ == '__main__':
    app.run(debug=True)

    
    