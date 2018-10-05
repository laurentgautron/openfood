import json
import mysql.connector
from connection import Connection

class CategoryProduct:

    @staticmethod
    def create():

        sql = """ CREATE TABLE IF NOT EXISTS category_product (
                            category_id INT,
                            product_code BIGINT,
                            PRIMARY KEY (category_id,product_code),
                            CONSTRAINT `fk_category_product_category` FOREIGN KEY (`category_id`) REFERENCES `category`(`id`),
                            CONSTRAINT `fk_category_product_product` FOREIGN KEY (`product_code`) REFERENCES `product`(`code`))
                            ENGINE = INNODB;
                        """
        with Connection.get_instance() as cursor:
            cursor.execute(sql)

    @staticmethod
    def insert():

        with open('openfoodbase.json', 'r') as f:
            datasopenfood = json.load(f)
        with Connection.get_instance() as cursor:
            for category, products in datasopenfood.items():
                sqlcat = """SELECT category.id FROM category
                            WHERE category.name = %s;"""
                cursor.execute(sqlcat, (category,))
                categoryId = cursor.fetchone()
                for code in products.keys():
                    sql = """INSERT INTO category_product(category_id, product_code) VALUES (%s,%s);"""
                    cursor.execute(sql, (categoryId[0], code))

    @staticmethod
    def get_datas(choiceCategory):

        sql = """SELECT product.name, code FROM product
                JOIN category_product ON product_code = code
                JOIN category ON category_id = category.id
                WHERE category.name = %s;"""
        with Connection.get_instance() as cursor:
            cursor.execute(sql, (choiceCategory[0],))
            productList = cursor.fetchall()
        return productList