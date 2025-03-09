from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/button')
def button():
    return render_template("button.html")

@app.route('/greeting')
def greeting():
    return render_template("greeting.html")

if __name__ == '__main__':
    app.run(debug=True)