
import json
import mysql.connector
import os
from connection import Connection

class Category:

    @staticmethod
    def create():

        sql = """ CREATE TABLE IF NOT EXISTS category (
                             id INT NOT NULL AUTO_INCREMENT,
                             name VARCHAR(100), 
                             PRIMARY KEY (id))
                             ENGINE = INNODB; 
                        """
        with Connection.get_instance() as cursor:
            cursor.execute(sql)

    @staticmethod
    def insert():

        with open('openfoodbase.json', 'r') as f:
            datasopenfood = json.load(f)
        for category in datasopenfood.keys():
            sql = """ INSERT INTO category(name) VALUES (%s);"""
            cursor.execute(sql, (category,))

    @staticmethod
    def get_datas():

        sql = """SELECT name, id FROM category;"""
        with Connection.get_instance() as cursor:
            cursor.execute(sql)
            categoryList = cursor.fetchall()
        return categoryList