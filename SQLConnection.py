import sqlite3

class SQLConn():
    # This method returns a connection to the SQLite database
    def connectToSQL():
        connection = sqlite3.connect('MotionDetection.db')
        return connection

    # This method ensures that the .db file has the necessary tables
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

    # this method checks the login information entered by 
    # the user. If the login information matches the entry 
    # in the database, it returns true. Else it returns false
    def checkLogin(connection, enteredUsr, enteredPass):
        cur = connection.cursor()
        checkPassQuery = """
                            SELECT Password FROM login
                            WHERE Login = ?
                            """
        cur.execute(checkPassQuery, (enteredUsr,))
        result = cur.fetchall()
        try:
            if(enteredPass == result[0][0]):
                cur.close()
                return True
            else:
                cur.close()
                return False
        except:
            return False

    # This method pulls the profile information 
    # of a user and returns it as an array
    def getProfile(connection, Login):
        cur = connection.cursor()
        getProfile = """
                        SELECT * FROM profile
                        WHERE Login = ?
                        """
        cur.execute(getProfile, Login)
        result = cur.fetchall()
        cur.close()
        return result

    # This method creates a login entry
    def createLogin(connection, user, passwd):
        cur = connection.cursor()
        makeLogin = """
                        INSERT INTO login (Login, Password)
                        VALUES(?, ?)
                        """
        cur.execute(makeLogin, (user, passwd))
        cur.close()

    # This method creates a profile entry
    def createProfile(connection, login, name, email, pin):
        cur = connection.cursor()
        makeProfile = """
                        INSERT INTO profile (Login, Name, Email, Pin)
                        VALUES(?, ?, ?, ?);
                        """
        cur.execute(makeProfile, (login, name, email, pin))
        cur.close()

    # This method changes a login password
    def changePassword(connection, login, oldPass, newPass):
        cur = connection.cursor()
        checkPassQuery = """
                            SELECT Password FROM login
                            WHERE Login = ?;
                            """
        cur.execute(checkPassQuery, (login,))
        result = cur.fetchall()
        try:
            if(oldPass == result[0][0]):
                changePass = """
                                UPDATE login
                                SET Password = ?
                                WHERE
                                    Login = ?;
                                """
                cur.execute(changePass, (login, newPass))
                cur.close()
                print('Changed')
                return True
            else:
                cur.close()
                print('Could not change')
                return False
        except:
            return False

    # This method changes a login password
    def changePIN(connection, login, oldPIN, newPIN):
        cur = connection.cursor()
        checkPassQuery = """
                            SELECT pin FROM profile
                            WHERE Login = ?;
                            """
        cur.execute(checkPassQuery, (login,))
        result = cur.fetchall()
        if(oldPIN == result[0][0]):
            changePIN = """
                            UPDATE profile
                            SET Pin = ?
                            WHERE
                                Login = ?;
                            """
            cur.execute(changePIN, (login, newPIN))
            cur.close()
            print('Changed')
            return True
        else:
            cur.close()
            print('Could not change')
            return False

    # This method fetches all login info
    def getLogins(connection):
        curr = connection.cursor()
        getLoginEntries = """
                            SELECT * FROM login;
                            """
        curr.execute(getLoginEntries)
        result = curr.fetchall()
        curr.close()
        return result

    # This method fetches all profiles
    def getProfiles(connection):
        cur = connection.cursor()
        getProfileEntries = """
                            SELECT * FROM profile;
                            """
        cur.execute(getProfileEntries)
        result = cur.fetchall()
        cur.close()
        return result

    # this method closes a connection to 
    # the SQLite database
    def closeConnection(connection):
        connection.close()
        return
