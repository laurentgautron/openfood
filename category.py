
import json
import mysql.connector
import os
#from categoryproduct import CategoryProduct

class Category:

    @staticmethod
    def create(db):

        sql = """ CREATE TABLE IF NOT EXISTS category (
                             id INT NOT NULL AUTO_INCREMENT,
                             name VARCHAR(100), 
                             PRIMARY KEY (id))
                             ENGINE = INNODB; 
                        """
        db.execute(sql)

    @staticmethod
    def insert(db):

        with open('openfoodbase.json', 'r') as f:
            datasopenfood = json.load(f)
        for category in datasopenfood.keys():
            sql = """ INSERT INTO category(name) VALUES (%s);"""
            db.execute(sql, (category,))

    @staticmethod
    def get_datas(db):

        sql = """SELECT name, id FROM category;"""
        db.execute(sql)
        categoryList = db.fetchall()
        return categoryList