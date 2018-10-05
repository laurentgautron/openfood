import mysql.connector
import atexit
import os

class Connection:
    INSTANCE = None

    def __init__(self):
        __class__.INSTANCE = self
        self.connection = mysql.connector.connect(host='localhost', user='lolo', password='cestmoi', database='openfoodbase')
        atexit.register(self.disconnect)

    def __enter__(self):
        self.cursor = self.connection.cursor(buffered=True)
        sqluse = "USE openfoodbase;"
        self.cursor.execute(sqluse)
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.connection.commit()

    def disconnect(self):
        self.connection.close()

    @classmethod
    def get_instance(cls):
        if cls.INSTANCE is None:
            cls()
        return cls.INSTANCE
