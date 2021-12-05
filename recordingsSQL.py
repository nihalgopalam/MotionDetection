import pandas
from SQLConnection import SQLConn

class logSQL():
    # This method returns a connection to the SQLite database
    def initTables():
        cur = SQLConn.connectToSQL()
        initTable = """
            DROP TABLE IF EXISTS recordings;
            CREATE TABLE recordings (
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        Date TEXT NOT NULL UNIQUE,
                        Start TEXT NOT NULL,
                        End TEXT NOT NULL);
            
        """
        cur.execute(initTable)
        return 

    def CSVtoSQL(csv, conn):
        pandas.read_csv(csv).to_sql("recordings", conn, if_exists='append', index=False)
        conn.execute("""SELECT * FROM recordingsl""")
        return conn.fetchall()