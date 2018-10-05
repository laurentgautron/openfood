import mysql.connector
from category import Category
from categoryProduct import CategoryProduct
from store import Store
from storeProduct import StoreProduct
from product import Product
from historic import Historic
from connection import Connection

class Tables:

    @staticmethod
    def creation():

        with Connection.get_instance() as cursor:
            sql = """ CREATE DATABASE IF NOT EXISTS openfoodbase CHARACTER SET utf8; """
            cursor.execute(sql)
        Category.create()
        Product.create()
        Store.create()
        CategoryProduct.create()
        StoreProduct.create()
        Historic.create()

    @staticmethod
    def fill_tables():

        Category.insert()
        Product.insert()
        Store.insert()
        CategoryProduct.insert()
        StoreProduct.insert()