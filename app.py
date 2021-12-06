from os import remove
from flask import Flask, render_template, request, jsonify, json, redirect
from flask.helpers import url_for
from SQLConnection import SQLConn
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/reset")
def reset():
    cur = SQLConn.connectToSQL()
    SQLConn.initTables(cur)
    print(SQLConn.getProfiles(cur))
    SQLConn.closeConnection(cur)
    return render_template("reset.html", flag = False)

@app.route("/reset_process", methods=["POST"])
def reset_process():
    cur = SQLConn.connectToSQL()
    SQLConn.initTables(cur)
    print(SQLConn.getProfiles(cur))
    if  request.method == "POST":
        username = request.form["new_user"]
        password = request.form["new_password"]
        print(username, password) 
        
    changed = SQLConn.changePassword(cur, username, password)
    SQLConn.closeConnection(cur)
    if changed:
        if changed == "Same Password":
            return render_template("reset.html", flag = "Same Password")
        else:
            return render_template("login.html", flag = False)
    else:
        return render_template("reset.html", flag = "Unable to Change")

    

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/register_process", methods=["POST"])
def register_process():
    cur = SQLConn.connectToSQL()
    SQLConn.initTables(cur)
    print(SQLConn.getProfiles(cur))
    if  request.method == "POST":
        email = request.form["new_email"]
        name = request.form["new_name"]
        username = request.form["new_user"]
        password = request.form["new_password"]
        pin = int(request.form["pin"])
        print(email, name, username, password, pin) 
        
    SQLConn.createProfile(cur, username, name, email, password, pin)
    SQLConn.closeConnection(cur)
    return render_template("login.html")


@app.route("/login")
def login():
    return render_template("login.html", flag = False)    

@app.route('/login_process', methods=['POST'])
def login_process():
    cur = SQLConn.connectToSQL()
    SQLConn.initTables(cur)
    if  request.method == "POST":
        username = request.form["UserID"]
        password = request.form["Password"]
        print(username, password) 
        
    credentials = SQLConn.checkLogin(cur, username, password)
    print(credentials, SQLConn.getProfileLogin(cur, username))
    SQLConn.closeConnection(cur)
    if credentials:
        return redirect(url_for("welcome", UserID = credentials[0][0]))
    else:
        return render_template("login.html", flag = "Wrong Credentials")
    

@app.route("/welcome/<UserID>")
def welcome(UserID):

    return render_template("welcome.html", user = UserID)


@app.route("/welcome/<UserID>/code")
def code(UserID):
    return render_template("code.html", user = UserID, flag = False)

@app.route("/welcome/<UserID>/code_process", methods=["POST"])
def code_process(UserID):
    cur = SQLConn.connectToSQL()
    SQLConn.initTables(cur)
    print(SQLConn.getProfiles(cur))
    ts = time.time()

    if  request.method == "POST":
        pin = request.form["pin"]
        print(pin, UserID) 
        
    credentials = SQLConn.checkPin(cur, UserID, pin)
    print(credentials, UserID)
    profile = SQLConn.getProfiles(cur)
    print(profile)
    SQLConn.closeConnection(cur)
    te = time.time()

    if credentials:
        return render_template("recordings.html", user = UserID, profile = profile)
    else:
        return render_template("code.html", user = UserID, flag = "Wrong Credentials")

@app.route("/welcome/<UserID>/recordings")
def recordings(UserID):
    cur = SQLConn.connectToSQL()
    profile = SQLConn.getProfiles(cur)
    SQLConn.closeConnection(cur)
    print(profile)
    return render_template("recordings.html", user = UserID, profile = profile)

@app.route("/welcome/<UserID>/logout")
def logout(UserID):
    return render_template("logout.html", user = UserID)  

@app.route("/welcome/<UserID>/logout_process")
def logout_process(UserID):
    print(UserID)
    cur = SQLConn.connectToSQL()
    SQLConn.initTables(cur)
    print(SQLConn.getProfiles(cur))
    SQLConn.delProfile(cur, UserID)
    SQLConn.closeConnection(cur)
    return render_template("logout.html", user = False)

@app.route("/welcome/<UserID>/stream")
def stream(UserID):
    return render_template("stream.html", user = UserID)  

if __name__ == "__main__":
    app.run(debug=True)