""" all opération cooresponding to a SQL code in product table """
import json
from connection import Connection

class Product:
    """ class category contain all methods concernig product table """
    @staticmethod
    def create():
        """ create table product """
        sql = """ CREATE TABLE IF NOT EXISTS product (
                    code BIGINT NOT NULL,
                    name VARCHAR(255),
                    nutri_score VARCHAR(1),
                    description TEXT(100),
                    link VARCHAR(255),
                    PRIMARY KEY(code))
                    ENGINE = INNODB; """
        with Connection.get_instance() as cursor:
            cursor.execute(sql)

    @staticmethod
    def insert():
        """ insert datas in table """
        with open('openfoodbase.json', 'r') as openfoodfile:
            datasopenfood = json.load(openfoodfile)
        listCodes = []
        with Connection.get_instance() as cursor:
            for datas in datasopenfood.values():
                for code, values in datas.items():
                    if code not in listCodes:
                        listCodes.append(code)
                        code = int(code)
                        datasProduct = (code, values['name'], values['nutri_score'], values['link'], values['description'])
                        sql = """INSERT INTO product(code, name, nutri_score, link, description)
                                VALUES (%s, %s, %s, %s, %s);"""
                        cursor.execute(sql, datasProduct)

    @staticmethod
    def propose_substitute(choiceCategory, code):
        """ find a substitute for a product: select all products with best nutri_score \
            and choose the last one , or the first with the best nutri-score : a """
        sqlresearch = """SELECT code, nutri_score FROM product \
                   JOIN category_product ON code = product_code \
                   JOIN category ON category.id = category_id \
                   WHERE category.name = %s AND product.nutri_score < (SELECT nutri_score FROM product WHERE code = %s);"""
        with Connection.get_instance() as cursor:
            cursor.execute(sqlresearch, (choiceCategory[0], code))
            result = cursor.fetchall()
        if len(result) > 0:
            bestScore = 'e'
            place = 0
            indice = 0
            while (indice < len(result)) and (bestScore != 'a'):
                if result[indice][1] < bestScore:
                    bestScore = result[indice][1]
                    place = indice
                indice += 1
            return result[place][0]
        else:
            print('There is no substitute for this product !!')
            return 0

    @staticmethod
    def show_details(product):
        """ show all field for a product code from product table """
        sql = """SELECT product.*, store.name FROM product \
                                JOIN store_product ON code_pro_store = code \
                                JOIN store ON store.id = id_store WHERE code = %s;"""
        with Connection.get_instance() as cursor:
            cursor.execute(sql, (product,))
            details = cursor.fetchone()
        return details
