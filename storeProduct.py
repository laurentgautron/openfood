import json
import mysql.connector

class StoreProduct:

    @staticmethod
    def create(db):

        sql = """ CREATE TABLE IF NOT EXISTS store_product (
                    id_store INT,
                    code_pro_store BIGINT,
                    PRIMARY KEY (id_store, code_pro_store),
                    CONSTRAINT `fk_store_product_name` FOREIGN KEY (`id_store`) REFERENCES `store`(`id`),
                    CONSTRAINT `fk_store_product_code` FOREIGN KEY (`code_pro_store`) REFERENCES `product`(`code`))
                     ENGINE = INNODB; """
        db.execute(sql)

    @staticmethod
    def insert(db):

        with open('openfoodbase.json', 'r') as f:
            datasopenfood = json.load(f)
        listCode = []
        for datascode in datasopenfood.values():
            for code, datas in datascode.items():
                if code not in listCode:
                    listCode.append(code)
                    for store in datas['store']:
                        sqlstore = "SELECT id FROM store WHERE name = %s;"
                        db.execute(sqlstore, (store,))
                        idStore = db.fetchone()
                        sql = """ INSERT INTO store_product(id_store, code_pro_store) VALUES (%s, %s); """
                        db.execute(sql, (idStore[0], code))