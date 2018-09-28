import mysql.connector
import atexit

class Connection:

    def __init__(self):

        self.connection = mysql.connector.connect(host='localhost', user='lolo', password='cestmoi')
        atexit.register(self.disconnect)

    def __enter__(self):

        self.cursor = self.connection.cursor(buffered=True)
        sql = "CREATE DATABASE IF NOT EXISTS openfoodbase CHARACTER SET utf8;"
        sqluse = "USE openfoodbase;"
        self.cursor.execute(sql)
        self.cursor.execute(sqluse)
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):

        self.cursor.close()
        self.connection.commit()
        print('Bye, to the next time')

    def disconnect(self):

        self.connection.close()
