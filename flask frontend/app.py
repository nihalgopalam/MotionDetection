from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/code")
def code():
    return render_template("code.html")

@app.route("/recordings")
def recordings():
    return render_template("recordings.html")

    
