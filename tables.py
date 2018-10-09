""" create and fill al tables at the beginning if openfoodbase.json does not exist ."""
from category import Category
from categoryproduct import CategoryProduct
from store import Store
from storeproduct import StoreProduct
from product import Product
from historic import Historic
from connection import Connection

class Tables:
    """ call static methods from class/tables to create and fill tables ."""
    @staticmethod
    def creation():
        """ create all the tables by calling static method from these tables
        six tables including two association tables:
        - CategoryProduct and StoreProduct ."""
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
        """ fill the tables after creation except historic table:
            five tables can be filled with the datas at the beginning ."""
        Category.insert()
        Product.insert()
        Store.insert()
        CategoryProduct.insert()
        StoreProduct.insert()
