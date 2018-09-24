import mysql.connector
import os
from category import Category

class Menu:

    def __init__(self):

        self.makeChoice = 'make your choice by choosing the corresponding number among the propositions !! '
        connection = mysql.connector.connect(host='localhost', user='lolo', password='cestmoi', database='openfoodbase')
        cursor = connection.cursor()
        sql = "SELECT name FROM category;"
        cursor.execute(sql)
        self.listCategory = cursor.fetchall()
        cursor.close()
        connection.close()

    def first_menu(self):

        os.system('clear')
        print('----- Main menu -----')
        print('1 - : consult a categories')
        print('2 - : consult historic')
        print('To quit , enter 0')
        print(self.makeChoice)
        choice = int(input('your choice is (enter a number beteween 1 and 3): '))
        while choice not in (0,1,2):
            try:
                choice = int(input())
            except ValueError as error:
                print('enter a numeral !!')
        return choice

    def second_menu(self):

        Category.menu()
        print('To return: r')
        print('To quit : 0')
        categoryChoice = int(input())
        return self.listCategory[categoryChoice-1]