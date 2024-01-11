import mysql.connector

class MySQL:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def create(self, sql, val):
        self.cursor.execute(sql, val)
        self.conn.commit()

    def read(self, sql):
        self.sql = sql
        self.cursor.execute(self.sql)

    def update(self, sql, val):
        self.cursor.execute(sql, val)
        self.conn.commit()

    def delete(self, sql):
        self.sql = sql
        self.cursor.execute(self.sql)
        self.conn.commit()

    def connection(self):
        self.conn = mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = self.database
        )

        self.cursor = self.conn.cursor()
        return self.cursor
    
    def disconnection(self):
        self.cursor.close()
        self.conn.close()
