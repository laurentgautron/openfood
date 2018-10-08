""" all requisites for a unique connextion for the application ."""
import atexit
import mysql.connector

class Connection:
    """ class to create unique connection and cursor for database openfoodbase ."""

    INSTANCE = None

    def __init__(self):
        """ construtor which modify INSTANCE form the class , and create database openfoodbase ."""
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
        """ create a cursor from 'with' instruction. """
        self.cursor = self.connection.cursor(buffered=True)
        sqluse = "USE openfoodbase;"
        self.cursor.execute(sqluse)
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        """ close cursor, and commit datas at end of 'with' ."""
        self.cursor.close()
        self.connection.commit()

    def disconnect(self):
        """ close connection ."""
        self.connection.close()

    @classmethod
    def get_instance(cls):
        """ return unique instance ."""
        if cls.INSTANCE is None:
            cls()
        return cls.INSTANCE
