""" all opération cooresponding to a SQL code in store table ."""
import json
from connection import Connection

class Store:
    """ class category contain all methods concernig store table ."""
    @staticmethod
    def create():
        """ create store table ."""
        sql = """ CREATE TABLE IF NOT EXISTS store (
                    id INT NOT NULL AUTO_INCREMENT,
                    name VARCHAR(255),
                    PRIMARY KEY(id))
                    ENGINE = INNODB; """
        with Connection.get_instance() as cursor:
            cursor.execute(sql)

    @staticmethod
    def insert():
        """ insert stores from the openfood json file , into store table ."""
        with open('openfoodbase.json', 'r') as openfoodfile:
            datas_openfood = json.load(openfoodfile)
        list_store = []
        with Connection.get_instance() as cursor:
            for data in datas_openfood.values():
                for datas in data.values():
                    for store in datas['store']:
                        if store not in list_store:
                            list_store.append(store)
                            sql = """ INSERT INTO store(name) VALUES (%s); """
                            cursor.execute(sql, (store,))
