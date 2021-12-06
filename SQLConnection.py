import sqlite3
from datetime import datetime, date

class SQLConn():
    # This method returns a connection to the SQLite database
    def connectToSQL():
        connection = sqlite3.connect('MotionDetection.db')
        return connection

    # This method ensures that the .db file has the necessary tables
    def initTables(connection):
        cur = connection.cursor()
        # login_schema = """
        #                 CREATE TABLE IF NOT EXISTS userLogin (
        #                 ID INTEGER PRIMARY KEY AUTOINCREMENT,
        #                 Login TEXT NOT NULL UNIQUE,
        #                 Password TEXT NOT NULL);
        #                 """
        profile_schema = """
                        CREATE TABLE IF NOT EXISTS profile (
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        Login TEXT NOT NULL UNIQUE,
                        Name TEXT NOT NULL,
                        Email TEXT NOT NULL,
                        Password TEXT NOT NULL,
                        Pin INTEGER);
                        """

        # cur.execute(login_schema)
        cur.execute(profile_schema)
        return

    # this method checks the login information entered by 
    # the user. If the login information matches the entry 
    # in the database, it returns true. Else it returns false
    def checkLogin(connection, enteredUsr, enteredPass):
        cur = connection.cursor()
        checkPassQuery = """
                            SELECT Name, Password FROM profile
                            WHERE Login = ?
                            """
        cur.execute(checkPassQuery, (enteredUsr,))
        result = cur.fetchall()
        if result:
            if(enteredPass == result[0][1]):
                return result
            else:
                return False
        else:
            return False

    def checkPin(connection, enteredUsr, pin):
        cur = connection.cursor()
        checkPassQuery = """
                            SELECT Pin FROM profile
                            WHERE Name = ?
                            """
        cur.execute(checkPassQuery, (enteredUsr,))
        result = cur.fetchall()
        print(result[0][0])
        try:
            if(int(pin) == result[0][0]):
                return result[0][0]
            else:
                return False
        except:
            return False


    # This method pulls the profile information 
    # of a user and returns it as an array
    def getProfileLogin(connection, Login):
        cur = connection.cursor()
        getProfileLogin = """
                        SELECT * FROM profile
                        WHERE Login = ?
                        """
        cur.execute(getProfileLogin, (Login,))
        result = cur.fetchall()
        return result

    def getProfileName(connection, name):
        cur = connection.cursor()
        getProfileName = """
                        SELECT * FROM profile
                        WHERE Name = ?
                        """
        cur.execute(getProfileName, (name,))
        result = cur.fetchall()
        return result

    # This method creates a profile entry
    def createProfile(connection, login, name, email, password, pin):
        cur = connection.cursor()
        makeProfile = """
                        INSERT INTO profile (Login, Name, Email, Password, Pin)
                        VALUES (?, ?, ?, ?, ?);
                        """
        cur.execute(makeProfile, (login, name, email, password, pin,))
        connection.commit()

    # This method changes a login password
    def changePassword(connection, login, newPass):
        cur = connection.cursor()
        checkPassQuery = """
                            SELECT Password FROM profile
                            WHERE Login = ?;
                            """
        cur.execute(checkPassQuery, (login,))
        result = cur.fetchall()
        if result:
            if not (newPass == result[0][0]):
                changePass = """
                                UPDATE profile
                                SET Password = ?
                                WHERE
                                    Login = ?;
                                """
                cur.execute(changePass, (newPass, login,))
                connection.commit()
                return "Changed"
            else:
                return "Same Password"
        else:
            return False

    # This method deletes a profile
    def delProfile(connection, name):
        cur = connection.cursor()
        print(name)
        deleteProfile = '''
                        DELETE FROM profile WHERE Name = ?;
        '''
        cur.execute(deleteProfile, (name,))
        connection.commit()
        print("deleted")


    # This method fetches all login info
    def getLogins(connection):
        curr = connection.cursor()
        getLoginEntries = """
                            SELECT Login, Password FROM profile;
                            """
        curr.execute(getLoginEntries)
        result = curr.fetchall()
        return result

    # This method fetches all profiles
    def getProfiles(connection):
        cur = connection.cursor()
        getProfileEntries = """
                            SELECT * FROM profile;
                            """
        cur.execute(getProfileEntries)
        result = cur.fetchall()
        return result

    # this method closes a connection to 
    # the SQLite database
    def closeConnection(connection):
        connection.close()
        return
