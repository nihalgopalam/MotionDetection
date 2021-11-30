from SQLConnection import SQLConn

class TestCases():
    def testF1(conn):
        SQLConn.createLogin(conn, 'al1234', 'password')
        print(SQLConn.getLogins(conn))
        SQLConn.createLogin(conn, 'nih1234', 'testpwd')
        print(SQLConn.getLogins(conn))
        SQLConn.createLogin(conn, 'ch1234', 'pwdtest')
        print(SQLConn.getLogins(conn))
        SQLConn.createLogin(conn, 'rut4321', 'rpwd')
        print(SQLConn.getLogins(conn))
        

    def testF2(conn):
        if(SQLConn.checkLogin(conn, 'al1234', 'password')):
            print('TRUE')
        else:
            print('FALSE')

        if(SQLConn.checkLogin(conn, 'al1234', 'notpwd')):
            print('TRUE')
        else:
            print('FALSE')

        if(SQLConn.checkLogin(conn, 'ch1234', 'pwdtest')):
            print('TRUE')
        else:
            print('FALSE')

        if(SQLConn.checkLogin(conn, 'ch1231', 'pwdtest')):
            print('TRUE')
        else:
            print('FALSE')

        if(SQLConn.checkLogin(conn, 'nih1234', 'testpwd')):
            print('TRUE')
        else:
            print('FALSE')

        if(SQLConn.checkLogin(conn, 'nih1234', 'password')):
            print('TRUE')
        else:
            print('FALSE')

    def testF3(conn):
        SQLConn.changePassword(conn, 'al1234', 'password', 'chngpwd')
        print(SQLConn.getLogins(conn))
        SQLConn.changePassword(conn, 'nih1234', 'testpwd', 'password')
        print(SQLConn.getLogins(conn))
        SQLConn.changePassword(conn, 'ch1234', 'pwdtest', 'newpwd')
        print(SQLConn.getLogins(conn))
        SQLConn.changePassword(conn, 'rut4321', 'rpwd', 'securepwd')
        print(SQLConn.getLogins(conn))


    def testCreateProfile(conn):
        SQLConn.createProfile(conn, 'al1234', 'Alan', 'alanjiang1139@gmail.com', 5678)
        print(SQLConn.getProfiles(conn))
        SQLConn.createProfile(conn, 'nih1234', 'Nihal', 'nihalgopalam@gmail.com', 9876)
        print(SQLConn.getProfiles(conn))
        SQLConn.createProfile(conn, 'ch1234', 'Chandra', 'chandrahas.nanduri1@gmail.com', 2345)
        print(SQLConn.getProfiles(conn))
        SQLConn.createProfile(conn, 'rut4321', 'Ruthvik', 'rvn.nunna@gmail.com', 4567)
        print(SQLConn.getProfiles(conn))

    def testF8(conn):
        SQLConn.changePIN(conn, 'al1234', 5687, 1234)
        print(SQLConn.getProfiles(conn))
        SQLConn.changePIN(conn, 'nih1234', 9876, 1234)
        print(SQLConn.getProfiles(conn))
        SQLConn.changePIN(conn, 'ch1234', 2345, 1234)
        print(SQLConn.getProfiles(conn))
        SQLConn.changePIN(conn, 'rut4321', 4567, 1234)
        print(SQLConn.getProfiles(conn))

conn = SQLConn.connectToSQL()
SQLConn.initTables(conn)
TestCases.testF1(conn)
TestCases.testF2(conn)
TestCases.testF3(conn)
TestCases.testCreateProfile(conn)
TestCases.testF8(conn)
SQLConn.closeConnection(conn)
