import json
import mysql.connector

class Product:

    @staticmethod
    def create():

        sql = """ CREATE TABLE IF NOT EXISTS product (
                    code BIGINT NOT NULL,
                    name VARCHAR(255),
                    nutri_score VARCHAR(1),
                    description TEXT(100),
                    link VARCHAR(255),
                    store VARCHAR(255),
                    PRIMARY KEY(code))
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
        connection = mysql.connector.connect(host='localhost', user='lolo', password='cestmoi', database='openfoodbase')
        cursor = connection.cursor()
        listCodes = []
        for datas in datasopenfood.values():
            for code, values in datas.items():
                if code not in listCodes:
                    listCodes.append(code)
                    stores = ','.join(values['store'])
                    datasProduct = (code,values['name'], values['nutri_score'],values['link'], stores, values['description'])
                    sql = """INSERT INTO product(code, name, nutri_score, link, store, description)
                            VALUES (%s, %s, %s, %s, %s, %s);"""
                    cursor.execute(sql, datasProduct)
        connection.commit()
        cursor.close()
        connection.close()
