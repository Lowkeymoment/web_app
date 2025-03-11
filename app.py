from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def find_last_name():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM users ORDER BY id DESC LIMIT 1")
    name = cursor.fetchall()[0][0]
    connection.commit()
    connection.close()
    return name

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/button')
def button():
    return render_template("button.html")

@app.route('/greeting')
def greeting():
    current_name = find_last_name()
    return render_template("greeting.html", name=current_name)

@app.route("/", methods=["POST"])
def form():
    name = request.form["name"]
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (name) VALUES (?)", (name,))
    connection.commit()
    connection.close()
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)