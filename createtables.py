

import mysql.connector

class Createtables:

    def __init__(self):

        self.connection = mysql.connector.connect(host = 'localhost', user = 'lolo', password = 'cestmoi')
        

    def create(self):

        sql_base = """ CREATE DATABASE IF NOT EXISTS openfoodbase CHARACTER SET 'utf8'; """

        sql_use = """ USE openfoodbase; """

        sql_category = """ CREATE TABLE IF NOT EXISTS category (
                             name VARCHAR(100), 
                             PRIMARY KEY (name))
                             ENGINE = INNODB DEFAULT CHARSET = 'utf8'; 
                        """

        sql_product =  """ CREATE TABLE IF NOT EXISTS product (
                            code BIGINT NOT NULL,
                            name VARCHAR(255),
                            nutri_score VARCHAR(1),
                            description TEXT(100),
                            link VARCHAR(255),
                            PRIMARY KEY(code))
                            ENGINE = INNODB DEFAULT CHARSET = 'utf8';
                        """

        sql_category_product = """ CREATE TABLE IF NOT EXISTS category_product (
                            category_name VARCHAR(100),
                            product_code BIGINT,
                            PRIMARY KEY (category_name,product_code),
                            CONSTRAINT `fk_category_product_category` FOREIGN KEY (`category_name`) REFERENCES `category`(`name`),
                            CONSTRAINT `fk_category_product_product` FOREIGN KEY (`product_code`) REFERENCES `product`(`code`))
                            ENGINE = INNODB DEFAULT CHARSET = 'utf8';
                        """

        sql_substitute = """ CREATE TABLE IF NOT EXISTS substitute (
                             code_product BIGINT NOT NULL,
                             substitute_code INT,
                             PRIMARY KEY(code_product))
                             ENGINE = INNODB DEFAULT CHARSET = 'utf8';
                        """

        sql_store = """ CREATE TABLE IF NOT EXISTS store (
                         name VARCHAR(25) NOT NULL,
                         PRIMARY KEY(name));
                    """

        sql_store_product = """ CREATE TABLE IF NOT EXISTS store_product (
                           name_store VARCHAR(25),
                           code_pro_store BIGINT,
                           PRIMARY KEY (name_store, code_pro_store),
                           CONSTRAINT `fk_store_product_name` FOREIGN KEY (`name_store`) REFERENCES `store`(`name`),
                           CONSTRAINT `fk_store_product_code` FOREIGN KEY (`code_pro_store`) REFERENCES `product`(`code`))
                           ENGINE = INNODB DEFAULT CHARSET = 'utf8';
                       """

    
        sql = [sql_base,sql_use,sql_category,sql_product,sql_category_product,sql_substitute,sql_store,sql_store_product]
        cursor = self.connection.cursor()
        for table in sql:
            cursor.execute(table)
        self.connection.commit()
        cursor.close()
        self.connection.close()
