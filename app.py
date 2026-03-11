from flask import Flask, render_template, request
import sqlite3
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    course = request.form['course']
    message = request.form['message']

    conn = sqlite3.connect('feedback.db')
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS feedback (name TEXT, course TEXT, message TEXT)")
    cursor.execute("INSERT INTO feedback VALUES (?, ?, ?)", (name, course, message))

    conn.commit()
    conn.close()

    return "Feedback Submitted Successfully!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)