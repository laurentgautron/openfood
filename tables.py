import mysql.connector
from category import Category
from categoryProduct import CategoryProduct
from store import Store
from storeProduct import StoreProduct
from product import Product
from historic import Historic

class Tables:

   
    def make_list_sql_create(self):

        return [self.category, self.product, self.store, self.categoryProduct, self.storeProduct, self.historic]

    @staticmethod
    def creation():

        connection = mysql.connector.connect(host='localhost', user='lolo', password='cestmoi')
        sql = """ CREATE DATABASE IF NOT EXISTS openfoodbase CHARACTER SET utf8; """
        cursor = connection.cursor()
        cursor.execute(sql)
        cursor.close()
        connection.close()
        Category.create()
        Product.create()
        Store.create()
        CategoryProduct.create()
        StoreProduct.create()
        Historic.create()

    def remove():

        connection = mysql.connector.connect(host='localhost', user='lolo', password='cestmoi')
        sql = """ DROP DATABASE openfoodbase; """
        cursor = connection.cursor()
        cursor.execute(sql)
        cursor.close()
        connection.close()

    def fill_tables():

        Category.insert()
        Product.insert()
        Store.insert()
        CategoryProduct.insert()
        StoreProduct.insert()