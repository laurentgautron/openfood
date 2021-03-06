""" all opération cooresponding to a SQL code in category table ."""
import json
from connection import Connection

class Category:
    """ class category contain all methods concernig category table ."""

    @staticmethod
    def create():
        """ method to create category table ."""
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
        """ method to inser datas in category table ."""

        with open('openfoodbase.json', 'r') as openfoodfile:
            datas_openfood = json.load(openfoodfile)
        with Connection.get_instance() as cursor:
            for category in datas_openfood.keys():
                sql = """ INSERT INTO category(name) VALUES (%s);"""
                cursor.execute(sql, (category,))

    @staticmethod
    def get_datas():
        """ method to get datas from category ."""

        sql = """SELECT name, id FROM category ORDER BY name;"""
        with Connection.get_instance() as cursor:
            cursor.execute(sql)
            category_list = cursor.fetchall()
        return category_list
