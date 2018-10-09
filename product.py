""" all opération cooresponding to a SQL code in product table ."""
import json
from connection import Connection

class Product:
    """ class category contain all methods concernig product table ."""
    @staticmethod
    def create():
        """ create table product """
        sql = """ CREATE TABLE IF NOT EXISTS product (
                    code BIGINT(13) NOT NULL,
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
        """ insert datas in table product ."""
        with open('openfoodbase.json', 'r') as openfoodfile:
            datas_openfood = json.load(openfoodfile)
        list_codes = []
        with Connection.get_instance() as cursor:
            for datas in datas_openfood.values():
                for code, values in datas.items():
                    if code not in list_codes:
                        list_codes.append(code)
                        code = int(code)
                        datas_product = (code, \
                                         values['name'], \
                                         values['nutri_score'], \
                                         values['link'], \
                                         values['description'])
                        sql = """INSERT INTO product(code, name, nutri_score, link, description)
                                VALUES (%s, %s, %s, %s, %s);"""
                        cursor.execute(sql, datas_product)

    @staticmethod
    def propose_substitute(choice_category, code):
        """ find a substitute for a product: select all products with best nutri_score \
            and choose the last one , or the first with the best nutri-score : a .
            return the product code for the substitute """
        sqlresearch = """SELECT code, nutri_score FROM product \
                   JOIN category_product ON code = product_code \
                   JOIN category ON category.id = category_id \
                   WHERE category.name = %s \
                   AND product.nutri_score < (SELECT nutri_score FROM product WHERE code = %s);"""
        with Connection.get_instance() as cursor:
            cursor.execute(sqlresearch, (choice_category[0], code))
            result = cursor.fetchall()
        if len(result) > 0:
            best_score = 'e'
            place = 0
            indice = 0
            while (indice < len(result)) and (best_score != 'a'):
                if result[indice][1] < best_score:
                    best_score = result[indice][1]
                    place = indice
                indice += 1
            return result[place][0]
        else:
            print('There is no substitute for this product !!')
            return 0

    @staticmethod
    def show_details(product):
        """ show all field for a product code from product table
            need a product: product code
            return details: dictionnary with yield and values for a product code.
            take store name in store table ."""
        sql = """SELECT product.*, store.name FROM product \
                                JOIN store_product ON code_pro_store = code \
                                JOIN store ON store.id = id_store WHERE code = %s;"""
        with Connection.get_instance() as cursor:
            cursor.execute(sql, (product,))
            details = cursor.fetchone()
        name_for_field = {}
        name_for_field['code'] = details[0]
        name_for_field['name'] = details[1]
        name_for_field['nutri_score'] = details[2]
        name_for_field['description'] = details[3]
        name_for_field['link'] = details[4]
        name_for_field['store'] = details[5]
        return name_for_field
