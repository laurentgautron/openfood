import mysql.connector
import json
from filter import Filter

class Operationonbase:

    def __init__(self):
        
        self.connection = mysql.connector.connect(host = 'localhost', user = 'lolo', password = 'cestmoi')
        self.store = Filter()
        
    def datas_in_tables(self):

        with open('openfoodbase.json','r') as openfoodfile:
            dataopenfood = json.load(openfoodfile)
        cursor = self.connection.cursor()
        listProducts = []
        listStore = []
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
                    storelist = value['store'].split(',')
                    storelist = self.store.filter_store(value['store'].split(','))    
                    for s in storelist:
                        if s not in listStore:
                            listStore.append(s)
                            sql_store = "INSERT INTO store(name) VALUES (%s);"
                            cursor.execute(sql_store, (s,))
                        sql_store_product = "INSERT INTO store_product(name_store,code_pro_store) VALUES (%s,%s);"
                        cursor.execute(sql_store_product, (s,code,))     
                sql_cat_product = "INSERT INTO category_product (category_name,product_code) VALUES (%s,%s);"
                cursor.execute(sql_cat_product, (cat,code,))
                print(listStore)
        print(len(listStore))
        self.connection.commit()
        cursor.close()
        self.connection.close()