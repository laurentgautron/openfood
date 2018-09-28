import json
import mysql.connector

class CategoryProduct:

    @staticmethod
    def create(db):

        sql = """ CREATE TABLE IF NOT EXISTS category_product (
                            category_id INT,
                            product_code BIGINT,
                            PRIMARY KEY (category_id,product_code),
                            CONSTRAINT `fk_category_product_category` FOREIGN KEY (`category_id`) REFERENCES `category`(`id`),
                            CONSTRAINT `fk_category_product_product` FOREIGN KEY (`product_code`) REFERENCES `product`(`code`))
                            ENGINE = INNODB;
                        """
        db.execute(sql)

    @staticmethod
    def insert(db):

        with open('openfoodbase.json', 'r') as f:
            datasopenfood = json.load(f)
        for category, products in datasopenfood.items():
            sqlcat = """SELECT category.id FROM category
                        WHERE category.name = %s;"""
            db.execute(sqlcat, (category,))
            categoryId = db.fetchone()
            for code in products.keys():
                sql = """INSERT INTO category_product(category_id, product_code) VALUES (%s,%s);"""
                db.execute(sql, (categoryId[0], code))

    @staticmethod
    def get_datas(db, choiceCategory):

        sql = """SELECT product.name, code FROM product
                JOIN category_product ON product_code = code
                JOIN category ON category_id = category.id
                WHERE category.name = %s;"""
        db.execute(sql, (choiceCategory[0],))
        productList = db.fetchall()
        return productList