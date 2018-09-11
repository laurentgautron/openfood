import mysql.connector
import json

class Insertdatas:

    def __init__(self):

        self.connection = mysql.connector.connect(host = 'localhost', user = 'lolo', password = 'cestmoi', database = 'openfoodbase')

    def category_product(self):

        with open('categories.json','r') as categoriesfile:
            datascategories = json.load(categoriesfile)
        with open('openfoodbase.json','r') as productsfile:
            dataproducts = json.load(productsfile)
        cursor = self.connection.cursor()
        for category in datascategories:
            cursor.execute(f"""INSERT INTO category (name) VALUES ("{category[0]}");""")
        self.connection.commit()
        cursor.close()
        self.connection.close()

    #def association_tables(self):


