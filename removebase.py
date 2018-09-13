import mysql.connector

class Remove:

    def __init__(self):

        self.connection = mysql.connector.connect(host = 'localhost', user = 'lolo', password = 'cestmoi')

    def remove_the_base(self):

        cursor = self.connection.cursor()
        cursor.execute("DROP DATABASE openfoodbase;")
        self.connection.commit()
        cursor.close()
        self.connection.close()