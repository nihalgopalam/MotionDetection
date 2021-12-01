from flask import Flask, render_template, request, url_for, flash, redirect
# from forms import LoginForm
import sqlite3

#database connection
def db_connection():
    conn = sqlite3.connect("MotionDetection.db")
    conn.row_factory = sqlite3.Row
    return conn

#create login and profile tables
def initTables(connection):
        cur = connection.cursor()
        login_schema = """
                        CREATE TABLE IF NOT EXISTS login (
                        ID INTEGER PRIMARY KEY,
                        Login TEXT NOT NULL UNIQUE,
                        Password TEXT NOT NULL);
                        """
        profile_schema = """
                        CREATE TABLE IF NOT EXISTS profile (
                        ID INTEGER PRIMARY KEY,
                        Login TEXT NOT NULL UNIQUE,
                        Name TEXT NOT NULL,
                        Email TEXT NOT NULL,
                        Pin INTEGER);
                        """
        
        cur.execute(login_schema)
        cur.execute(profile_schema)
        cur.close()
        return

app = Flask(__name__)
app.debug = True

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/login", methods=("GET", "POST"))
def login():
    error = None
    
    if request.method == "POST":
        UserID = request.form['UserID']
        Password = request.form['Password']
        db=sqlite3.connect('MotionDetection.db')
        initTables(db)

        #test
        exampleLogin_Schema = """
                        INSERT INTO login(ID, Login, Password) VALUES('1', 'nihal', 'gopalam');
                        """

        cur = db.cursor()
        checkPassQuery = """
                            SELECT Password FROM login
                            WHERE Login = ?
                            """
        cur.execute(checkPassQuery, UserID)
        result = cur.fetchall()

        #test 
        exampleLogout_Schema = """
                        DELETE FROM login WHERE Login = 'nihal';
                        """

        if(Password == result[0]):
            cur.close()
            flash("Logged In")
            return redirect(url_for("home"))
        else:
            cur.close()
            flash("Invalid")

    return render_template("login.html")    

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

    
