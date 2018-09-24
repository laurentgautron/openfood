import json
import mysql.connector

class CategoryProduct:

    @staticmethod
    def create():

        sql = """ CREATE TABLE IF NOT EXISTS category_product (
                            category_name VARCHAR(100),
                            product_code BIGINT,
                            PRIMARY KEY (category_name,product_code),
                            CONSTRAINT `fk_category_product_category` FOREIGN KEY (`category_name`) REFERENCES `category`(`name`),
                            CONSTRAINT `fk_category_product_product` FOREIGN KEY (`product_code`) REFERENCES `product`(`code`))
                            ENGINE = INNODB;
                        """
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
        for category, products in datasopenfood.items():
            for code in products.keys():
                sql = """INSERT INTO category_product(category_name, product_code) VALUES (%s,%s);"""
                cursor.execute(sql, (category, code,))
        connection.commit()
        cursor.close()
        connection.close()

    def menu(categoryChoice):

        connection = mysql.connector.connect(host='localhost', user='lolo', password='cestmoi', database='openfoodbase')
        cursor = connection.cursor()
        sql = """SELECT product.name FROM product JOIN category_product ON product_code = code \
                    WHERE category_name = %s;"""
        cursor.execute(sql, categoryChoice)
        products = cursor.fetchall()
        connection.commit()
        cursor.close()
        connection.close()
        for indice, product in enumerate(products):
            print('%d - : %s'%(indice+1, product[0]))