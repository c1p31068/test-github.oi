from flask import Flask
from flask import render_template
from flask import Flask, request, render_template
from flask import Flask, render_template, request, redirect, url_for
import os
import sqlite3
import cv2
import numpy as np
from PIL import Image
import subprocess





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




#フロントのHTMLです。最初に表示したいページはここを変えてね。
@app.route("/")
def index():
    conn = sqlite3.connect('comments.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM comments')
    comments = cursor.fetchall()

    conn.close()
    #ここの.htmlを変える。
    return render_template('commander.html', comments=comments)


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

@app.route("/view_comments")
def view_comments():
    # SQLiteデータベースに接続
    conn = sqlite3.connect('comments.db')
    cursor = conn.cursor()

    # データベースからコメントを取得
    cursor.execute('SELECT * FROM comments')
    comments = cursor.fetchall()

    # データベース接続をクローズ
    conn.close()

    # 取得したコメントをHTMLテンプレートに渡して表示
    return render_template('view_comments.html', comments=comments)

#HTMLのページ管理

@app.route("/student", methods=["GET"])
def student():
    uploaded_files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('student.html', uploaded_files=uploaded_files)


@app.route("/instructor", methods=["GET"])
def instructor():
    uploaded_files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('instructor.html', uploaded_files=uploaded_files)



@app.route("/hello", methods=["GET"])
def hello_world():
    uploaded_files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('hello.html', uploaded_files=uploaded_files)


@app.route('/run_script', methods=['POST'])
def run_script():
    # ボタンがクリックされたときに実行するPythonスクリプトのパス
    script_path = 'cmp.py'

    # Pythonスクリプトを実行する
    result = subprocess.run(['python', script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    return render_template('hello.html')

@app.route('/run_script2', methods=['POST'])
def run_script2():
    # ボタンがクリックされたときに実行するPythonスクリプトのパス
    script_path = 'tsuchiya8.py'

    # Pythonスクリプトを実行する
    result = subprocess.run(['python', script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    return render_template('hello.html', result=result.stdout,error_output=result.stderr)







@app.route("/bronze", methods=["GET"])
def chimu():
    uploaded_files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('chinu.html', uploaded_files=uploaded_files)


@app.route('/submit_response', methods=['POST'])
def submit_response():
    name = request.form.get('name')
    answer = request.form.get('answer')

    if name and answer:
        conn = sqlite3.connect('responses.db')
        cursor = conn.cursor()

        cursor.execute('INSERT INTO responses (name, answer) VALUES (?, ?)', (name, answer))
        conn.commit()

        conn.close()

    return redirect(url_for('index'))



@app.route("/responses")
def view_responses():
    conn = sqlite3.connect('responses.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM responses')
    responses = cursor.fetchall()

    conn.close()

    return render_template('responses.html', responses=responses)





#↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑ここまででファイルを増やしてください↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'ファイルがありません'

    file = request.files['file']

    if file.filename == '':
        return render_template('no.html')

    if file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)

        # ファイルがすでに存在するか確認
        if os.path.exists(filename):
            # 既存のファイルと同じ名前のファイルが存在する場合のエラーハンドリング
            return render_template('file_exists_error.html', error_message="ファイルが既に存在します")
        
        file.save(filename)
        path2 = 'uploads/ent_kaito.mp4'
        os.rename(filename,path2)
        return render_template('zumi.html')
    





@app.route('/delete/<filename>', methods=['GET'])
def delete_file(filename):
    try:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        os.remove(filepath)
        return render_template('dl.html')
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
