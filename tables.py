import mysql.connector
from category import Category
from categoryProduct import CategoryProduct
from store import Store
from storeProduct import StoreProduct
from product import Product
from historic import Historic

class Tables:

    @staticmethod
    def creation(db):

        sql = """ CREATE DATABASE IF NOT EXISTS openfoodbase CHARACTER SET utf8; """
        db.execute(sql)
        Category.create(db)
        Product.create(db)
        Store.create(db)
        CategoryProduct.create(db)
        StoreProduct.create(db)
        Historic.create(db)

    @staticmethod
    def fill_tables(db):

        Category.insert(db)
        Product.insert(db)
        Store.insert(db)
        CategoryProduct.insert(db)
        StoreProduct.insert(db)