import json
import mysql.connector

class Historic:

    @staticmethod
    def create():

        sql = """ CREATE TABLE IF NOT EXISTS historic (
                    code_to_substitute BIGINT NOT NULL,
                    substitute_name VARCHAR(255),
                    PRIMARY KEY (code_to_substitute))
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