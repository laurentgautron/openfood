import os
import mysql.connector

class Menu:

    def __init__(self):

        self.how_to_exit = 'if you want exit the application enter 0 !'
        self.connection = mysql.connector.connect(host='localhost', user='lolo', password='cestmoi', database='openfoodbase')
        self.make_choice = 'make your choice by choosing the corresponding number among the propositions: '

    def first_menu(self):

        category_choice = int
        while category_choice not in [0, 1, 2]:
            try:
                os.system("clear")
                print(self.how_to_exit) 
                print('-------- Main menu --------')
                print('1 - : consult the categories')
                print('2 - : consult the history')
                category_choice = int(input(self.make_choice))
            except ValueError as exeption:
                continue
        return category_choice

    def next_menu(self, menu_choice):

        cursor = self.connection.cursor()
        os.system("clear")
        print(self.how_to_exit)
        self.menu_choice = menu_choice
        print(self.menu_choice)
        print('------ %s ------'%self.menu_choice)
        sql = "SELECT name FROM %s;"%self.menu_choice
        cursor.execute(sql)
        rows = cursor.fetchall()
        self.connection.commit()
        cursor.close()
        for number, value in enumerate(rows):
            value_list = list(value)[0]
            print(' %d - : %s'%(number+1, value_list))
        return rows[int(input(self.make_choice))-1]
