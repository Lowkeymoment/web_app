from package import app
from flask import render_template

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/button')
def button():
    return render_template("button.html")

@app.route('/profile')
def greeting():
    current_username = "Placeholder"
    return render_template("profile.html", name=current_username)

@app.route("/", methods=["POST"])
def form():
    # Getting the user into the database
    return render_template("index.html")