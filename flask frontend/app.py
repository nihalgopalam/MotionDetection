from flask import Flask, render_template, request, url_for, flash, redirect
from flask.wrappers import Request
# from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
# from forms import LoginForm
import sqlite3
import import messagebox

def db_connection():
    conn = sqlite3.connect("MotionDetection.db")
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__)
app.debug = True
app.config['SECRET']

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/login", methods=("GET", "POST"))
def login():
    if request.method == "POST":
        UserID = request.form['UserID']
        Password = request.form['Password']

     global counter
    db=sqlite3.connect('MotionDetection.db')
    cursor=db.cursor()
    cursor.execute("SELECT * FROM login where Login=? AND Password=?", (request.form['UserID'], request.form['Password'])
    row=cursor.fetchone()
    if row:
        messagebox.showinfo('info', 'login successful')
        counter=0
    else:
        messagebox.showinfo('info', 'login failed')
        counter+=1
        if counter>=3:
            exit()
    cursor.connection.commit()
    db.close()



    return render_template("login.html")    # add the result of the login to render_template ex. ("login.html", success)

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

    
