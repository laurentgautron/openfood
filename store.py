import json
import mysql.connector

class Store:


    @staticmethod

    def create(db):

        sql = """ CREATE TABLE IF NOT EXISTS store (
                    id INT NOT NULL AUTO_INCREMENT,
                    name VARCHAR(255),
                    PRIMARY KEY(id))
                    ENGINE = INNODB; """
        db.execute(sql)

    @staticmethod
    def insert(db):

        with open('openfoodbase.json', 'r') as f:
            datasopenfood = json.load(f)
        listStore = []
        for data in datasopenfood.values():
            for datas in data.values():
                for store in datas['store']:
                    if store not in listStore:
                        listStore.append(store)
                        sql = """ INSERT INTO store(name) VALUES (%s); """
                        db.execute(sql, (store,))

    #@staticmethod
    #def get_datas(db, code):