import mysql.connector
import json


class Operationonbase:

    def __init__(self):
        
        self.connection = mysql.connector.connect(host = 'localhost', user = 'lolo', password = 'cestmoi')
        

    def datas_in_tables(self):

        with open('openfoodbase.json','r') as openfoodfile:
            dataopenfood = json.load(openfoodfile)
        cursor = self.connection.cursor()
        listProducts = []
        cursor.execute("USE openfoodbase;")
        for cat, products in dataopenfood.items():
            sql_cat = "INSERT INTO category(name) VALUES (%s);"
            cursor.execute(sql_cat, (cat,))
            for code,value in products.items():
                if code not in listProducts:
                    listProducts.append(code)
                    datas = (code,value['name'],value['nutri_score'],value['description'],value['link'])
                    sql_datas = "INSERT INTO product(code,name,nutri_score,description,link) VALUES (%s,%s,%s,%s,%s);"
                    cursor.execute(sql_datas,datas)
                else:
                    continue
        self.connection.commit()
        cursor.close()
        self.connection.close()

    def remove(self):

        cursor = self.connection.cursor()
        cursor.execute("DROP DATABASE openfoodbase;")
        self.connection.commit()
        cursor.close()
        self.connection.close()