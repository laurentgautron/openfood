import json
import mysql.connector
from connection import Connection

class Store:


    @staticmethod

    def create():

        sql = """ CREATE TABLE IF NOT EXISTS store (
                    id INT NOT NULL AUTO_INCREMENT,
                    name VARCHAR(255),
                    PRIMARY KEY(id))
                    ENGINE = INNODB; """
        with Connection.get_instance() as cursor:
            cursor.execute(sql)

    @staticmethod
    def insert():

        with open('openfoodbase.json', 'r') as f:
            datasopenfood = json.load(f)
        listStore = []
        with Connection.get_instance() as cursor:
            for data in datasopenfood.values():
                for datas in data.values():
                    for store in datas['store']:
                        if store not in listStore:
                            listStore.append(store)
                            sql = """ INSERT INTO store(name) VALUES (%s); """
                            cursor.execute(sql, (store,))