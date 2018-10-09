""" all opération cooresponding to a SQL code in category_product table ."""
import json
from connection import Connection

class CategoryProduct:
    """ class category contain all methods concernig category_product table ."""
    @staticmethod
    def create():
        """ method to create catagory_product table """
        sql = """ CREATE TABLE IF NOT EXISTS category_product (
                            category_id INT,
                            product_code BIGINT(13),
                            PRIMARY KEY (category_id,product_code),
                            CONSTRAINT `fk_category_product_category` FOREIGN KEY (`category_id`) REFERENCES `category`(`id`),
                            CONSTRAINT `fk_category_product_product` FOREIGN KEY (`product_code`) REFERENCES `product`(`code`))
                            ENGINE = INNODB;"""
        with Connection.get_instance() as cursor:
            cursor.execute(sql)

    @staticmethod
    def insert():
        """ method to insert datas in category_product table ."""
        with open('openfoodbase.json', 'r') as openfoodfile:
            datas_openfood = json.load(openfoodfile)
        with Connection.get_instance() as cursor:
            for category, products in datas_openfood.items():
                sqlcat = """SELECT category.id FROM category
                            WHERE category.name = %s;"""
                cursor.execute(sqlcat, (category,))
                category_id = cursor.fetchone()
                for code in products.keys():
                    sql = """ INSERT INTO category_product(category_id, product_code)\
                             VALUES (%s,%s); """
                    cursor.execute(sql, (category_id[0], code))

    @staticmethod
    def get_datas(choice_category):
        """ method to get datas from category_product table ."""
        sql = """SELECT product.name, code FROM product
                JOIN category_product ON product_code = code
                JOIN category ON category_id = category.id
                WHERE category.name = %s ORDER BY name;"""
        with Connection.get_instance() as cursor:
            cursor.execute(sql, (choice_category[0],))
            product_list = cursor.fetchall()
        return product_list
