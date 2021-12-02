from flask import Flask, render_template, request, jsonify
# from forms import LoginForm
from SQLConnection import SQLConn



app = Flask(__name__)
app.debug = True


@app.route("/")
def index():
    return render_template("home.html")

@app.route("/login", methods=("GET", "POST"))
def login():
    return render_template("login.html")    

@app.route("/login_process", methods=["POST"])
def loginProcess():
    cur = SQLConn.connectToSQL()
    if request.method == "POST":
        info = request.get_json()
    SQLConn.closeConnection(cur)
    return jsonify(info)
        #check with db here

@app.route("/welcome")
def welcome():
    return render_template("welcome.html")

@app.route("/code")
def code():
    return render_template("code.html")

@app.route("/recordings")
def recordings():
    return render_template("recordings.html")

@app.route("/reset")
def reset():
    return render_template("reset.html")

@app.route("/register")
def register():
    return render_template("register.html")


