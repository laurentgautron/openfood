import mysql.connector
import json


connection = mysql.connector.connect(host = 'localhost', user = 'lolo', password = 'cestmoi', database = 'openfoodbase')
with open('categories.json','r') as categoriesfile:
    datascategories = json.load(categoriesfile)
with open('openfoodbase.json','r') as openfoodfile:
    dataopenfood = json.load(openfoodfile)

cursor = connection.cursor()
listProducts = []
for category, products in dataopenfood.items():
    cursor.execute(f"""INSERT INTO category (name) VALUES ("{category}");""")
    for code,value in products.items():
        if code not in listProducts:
            listProducts.append(code)
            print(code)
            cursor.execute(f"""INSERT INTO product (code,name,nutri_score,description,link) VALUES ("{code}","{value['name']}","{value['nutri_score']}","{value['description']}","{value['link']}");""")
        else:
            continue
connection.commit()
cursor.close()
connection.close()