import json
import mysql.connector

class StoreProduct:

    @staticmethod
    def create():

        sql = """ CREATE TABLE IF NOT EXISTS store_product (
                    name_store VARCHAR(25),
                    code_pro_store BIGINT,
                    PRIMARY KEY (name_store, code_pro_store),
                    CONSTRAINT `fk_store_product_name` FOREIGN KEY (`name_store`) REFERENCES `store`(`name`),
                    CONSTRAINT `fk_store_product_code` FOREIGN KEY (`code_pro_store`) REFERENCES `product`(`code`))
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
        listCode = []
        for datascode in datasopenfood.values():
            for code, datas in datascode.items():
                if code not in listCode:
                    listCode.append(code)
                    for store in datas['store']:
                        if store.split() != []:
                            sql = """ INSERT INTO store_product(name_store, code_pro_store) VALUES (%s, %s); """
                            cursor.execute(sql, (store, code))
        connection.commit()
        cursor.close()
        connection.close()