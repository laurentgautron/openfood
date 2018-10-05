import mysql.connector
import atexit
import os

class Connection:
    INSTANCE = None

    def __init__(self):
        __class__.INSTANCE = self
        config = {'host':'localhost'}
        userName = input('your username : ')
        pwd = input('our password : ')
        config['user'] = userName
        config['password'] = pwd
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()
        sql = "CREATE DATABASE IF NOT EXISTS openfoodbase CHARACTER SET utf8"
        self.cursor.execute(sql)
        self.cursor.close()
        self.connection.commit()
        self.connection.close()
        config['database'] = 'openfoodbase'
        self.connection = mysql.connector.connect(**config)
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
