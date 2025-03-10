from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)
connection = sqlite3.connect("database.db")
cursor = connection.cursor()

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/button')
def button():
    return render_template("button.html")

@app.route('/greeting')
def greeting():
    return render_template("greeting.html")

@app.route("/", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form["name"]
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name) VALUES (?)", (name,))
        conn.commit()
        conn.close()
        return "Data saved successfully!"

if __name__ == '__main__':
    app.run(debug=True)