import mysql.connector

connection = mysql.connector.connect(host = 'localhost', user = 'lolo', password = 'cestmoi', database = 'openfoodbase')

listp = ['Pierre','Laurent']
cursor = connection.cursor()
for i in listp:
	cursor.execute("INSERT INTO category (name) VALUES ('?')", i)
connection.commit()
cursor.close()
connection.close()
