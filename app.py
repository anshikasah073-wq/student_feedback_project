from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def create_table():
    conn = sqlite3.connect('feedback.db')
    c = conn.cursor()

    c.execute('''
    CREATE TABLE IF NOT EXISTS feedback(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        course TEXT,
        message TEXT
    )
    ''')

    conn.commit()
    conn.close()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():

    name = request.form['name']
    course = request.form['course']
    message = request.form['message']

    conn = sqlite3.connect('feedback.db')
    c = conn.cursor()

    c.execute("INSERT INTO feedback (name, course, message) VALUES (?,?,?)",
              (name, course, message))

    conn.commit()
    conn.close()

    return "Thank you! Your feedback has been submitted."

if __name__ == "__main__":
    create_table()
    app.run(host="0.0.0.0", port=10000)