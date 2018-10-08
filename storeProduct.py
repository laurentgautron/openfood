""" all opération cooresponding to a SQL code in store_product table ."""
import json
from connection import Connection

class StoreProduct:
    """ class category contain all methods concernig store_product table ."""
    @staticmethod
    def create():
        """ create store_product table"""
        sql = """ CREATE TABLE IF NOT EXISTS store_product (
                    id_store INT,
                    code_pro_store BIGINT,
                    PRIMARY KEY (id_store, code_pro_store),
                    CONSTRAINT `fk_store_product_name` FOREIGN KEY (`id_store`) REFERENCES `store`(`id`),
                    CONSTRAINT `fk_store_product_code` FOREIGN KEY (`code_pro_store`) REFERENCES `product`(`code`))
                     ENGINE = INNODB; """
        with Connection.get_instance() as cursor:
            cursor.execute(sql)

    @staticmethod
    def insert():
        """ insert datas from openfood json file into store_product ."""
        with open('openfoodbase.json', 'r') as openfoodfile:
            datasopenfood = json.load(openfoodfile)
        listCode = []
        with Connection.get_instance() as cursor:
            for datascode in datasopenfood.values():
                for code, datas in datascode.items():
                    if code not in listCode:
                        listCode.append(code)
                        for store in datas['store']:
                            sqlstore = "SELECT id FROM store WHERE name = %s;"
                            cursor.execute(sqlstore, (store,))
                            idStore = cursor.fetchone()
                            sql = """ INSERT INTO store_product(id_store, code_pro_store) \
                                      VALUES (%s, %s); """
                            cursor.execute(sql, (idStore[0], code))
