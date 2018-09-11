

import mysql.connector

class Createtables:

    def __init__(self):
        self.connection = mysql.connector.connect(host = 'localhost', user = 'lolo', password = 'cestmoi')
        

    def create(self):

        sql_base = """ CREATE DATABASE openfoodbase CHARACTER SET 'utf8'; """

        sql_use = """ USE openfoodbase; """

        sql_category = """ CREATE TABLE category (
                             name VARCHAR(100) , 
                             PRIMARY KEY (name))
                             ENGINE = INNODB DEFAULT CHARSET = 'utf8'; 
                        """

        sql_product =  """ CREATE TABLE product (
                            code INT NOT NULL,
                            store VARCHAR(45),
                            nutri_score VARCHAR(1),
                            description TEXT(100),
                            link VARCHAR(45),
                            PRIMARY KEY(code))
                            ENGINE = INNODB DEFAULT CHARSET = 'utf8';
                        """

        sql_category_product = """ CREATE TABLE category_product (
                            category_name VARCHAR(100),
                            product_code INT,
                            PRIMARY KEY (category_name,product_code),
                            CONSTRAINT `fk_category_product_category` FOREIGN KEY (`category_name`) REFERENCES `category`(name),
                            CONSTRAINT `fk_category_product_product` FOREIGN KEY (`product_code`) REFERENCES `product`(`code`))
                            ENGINE = INNODB DEFAULT CHARSET = 'utf8';
                        """

        sql_substitute = """ CREATE TABLE substitute (
                             code_product INT NOT NULL,
                             substitute_code INT,
                             PRIMARY KEY(code_product))
                             ENGINE = INNODB DEFAULT CHARSET = 'utf8';
                        """

        sql_store = """ CREATE TABLE store (
                         name VARCHAR(25) NOT NULL,
                         PRIMARY KEY(name));
                    """

        sql_store_product = """ CREATE TABLE store_product (
                           name_store VARCHAR(25),
                           code_pro_store INT,
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
        self.connection.close()
