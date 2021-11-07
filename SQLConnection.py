import sqlite3

class SQLConnection():
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
        cur.execute(checkPassQuery, enteredUsr)
        result = cur.fetchall()
        if(enteredPass == result[0]):
            cur.close()
            return True
        else:
            cur.close()
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
      
    # this method closes a connection to 
    # the SQLite database
    def closeConnection(connection):
        connection.close()
        return
