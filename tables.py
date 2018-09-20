import mysql.connector
from category import Category
from categoryProduct import CategoryProduct
from store import Store
from storeProduct import StoreProduct
from product import Product
from historic import Historic

class Tables:

    def __init__(self):

        self.category = Category.create()
        self.product = Product.create()
        self.store = Store.create()
        self.categoryProduct = CategoryProduct.create()
        self.storeProduct = StoreProduct.create()
        self.historic = Historic.create()
        

    def make_list_sql_create(self):

        return [self.category, self.product, self.store, self.categoryProduct, self.storeProduct, self.historic]

    @staticmethod
    def creation(listables):

        connection = mysql.connector.connect(host='localhost', user='lolo', password='cestmoi')
        sql_base = """ CREATE DATABASE IF NOT EXISTS openfoodbase DEFAULT CHARACTER SET utf8; """
        sql_use = """ USE openfoodbase; """
        cursor = connection.cursor()
        cursor.execute(sql_base)
        cursor.execute(sql_use)
        for tables in listables:
            cursor.execute(tables)
        cursor.close()
        connection.close()

    def remove():

        connection = mysql.connector.connect(host='localhost', user='lolo', password='cestmoi')
        sql_drop = """ DROP DATABASE openfoodbase; """
        cursor = connection.cursor()
        cursor.execute(sql_drop)
        cursor.close()
        connection.close()