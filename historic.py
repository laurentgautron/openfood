import json
import mysql.connector
from connection import Connection

class Historic:

    @staticmethod
    def create():

        sql = """ CREATE TABLE IF NOT EXISTS historic (
                    code_to_substitute BIGINT NOT NULL,
                    substitute_code BIGINT,
                    PRIMARY KEY (code_to_substitute))
                    ENGINE = INNODB; """
        with Connection.get_instance() as cursor:
            cursor.execute(sql)

    @staticmethod
    def insert(substitute, code):

        with Connection.get_instance() as cursor:
            sql = "SELECT count(code_to_substitute) FROM historic WHERE code_to_substitute = %s;"
            cursor.execute(sql, (code,))
            test = cursor.fetchone()
            if test[0]==0:
                sql = """INSERT INTO historic (code_to_substitute, substitute_code) VALUES (%s, %s);"""
                cursor.execute(sql, (code, substitute))
            else:
                print('you\'ve already made a research for this food')

    @staticmethod
    def get_datas():

        with Connection.get_instance() as cursor:
            sql = """SELECT * FROM historic;"""
            cursor.execute(sql)
            codeSubstitute = cursor.fetchall()
        return codeSubstitute

