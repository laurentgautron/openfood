import mysql.connector

class Tables:


    @staticmethod
    def creation(listables):

        connection = mysql.connector.connect(host='localhost', user='lolo', password='cestmoi')
        sql_base = """ CREATE DATABASE IF NOT EXISTS openfoodbase DEFAULT CHARACTER SET utf8; """
        sql_use = """ USE openfoodbase; """
        cursor = connection.cursor()
        cursor.execute(sql_base)
        cursor.execute(sql_use)
        for tables in listables:
            cursor.execute(tables)
        cursor.close()
        connection.close()

    def remove():

        connection = mysql.connector.connect(host='localhost', user='lolo', password='cestmoi')
        sql_drop = """ DROP DATABASE openfoodbase; """
        cursor = connection.cursor()
        cursor.execute(sql_drop)
        cursor.close()
        connection.close()