import mysql.connector
import json


class Insertdatas:

    def __init__(self):
        connection = mysql.connector.connect(host = 'localhost', user = 'lolo', password = 'cestmoi')
        

    def datas_in_tables(self):

        with open('openfoodbase.json','r') as openfoodfile:
            dataopenfood = json.load(openfoodfile)
        cursor = connection.cursor()
        listProducts = []
        cursor.execute("USE openfoodbase;")
        for category, products in dataopenfood.items():
            cursor.execute("INSERT INTO category (name) VALUES (%s);", category)
            for code,value in products.items():
                if code not in listProducts:
                    listProducts.append(code)
                    cursor.execute("INSERT INTO product (code,name,nutri_score,description,link) VALUES (%s,%s,%s,%s,%s);", 
                        code,value['name'],value['nutri_score'],value['description'],value['link'])
                else:
                    continue
        connection.commit()
        cursor.close()
        connection.close()