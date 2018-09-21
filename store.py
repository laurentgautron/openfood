import json
import mysql.connector

class Store:


    @staticmethod

    def create():

        sql = """ CREATE TABLE IF NOT EXISTS store (
                    name VARCHAR(255) NOT NULL,
                    PRIMARY KEY(name))
                    ENGINE = INNODB; """
        connection = mysql.connector.connect(host='localhost', user='lolo', password='cestmoi', database='openfoodbase')
        sql_use = """ USE openfoodbase; """
        cursor = connection.cursor()
        cursor.execute(sql_use)
        cursor.execute(sql)
        connection.commit()
        cursor.close()
        connection.close()

    def insert():

        with open('openfoodbase.json', 'r') as f:
            datasopenfood = json.load(f)
        listStore = []
        connection = mysql.connector.connect(host='localhost', user='lolo', password='cestmoi', database='openfoodbase')
        cursor = connection.cursor()
        for data in datasopenfood.values():
            for datas in data.values():
                for store in datas['store']:
                    if store not in listStore:
                        listStore.append(store)
                        sql = """ INSERT INTO store(name) VALUES (%s); """
                        cursor.execute(sql, (store,))
        connection.commit()
        cursor.close()
        connection.close()
