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

    #def is_valid(self,choice):


    def first_menu(self):

        os.system('clear')
        print('----- Main menu -----')
        print('1 - : consult a categories')
        print('2 - : consult historic')
        print('To quit , enter 0')
        print(self.makeChoice)
        choice = input('your choice is (enter a number beteween 1 and 2): ')
        #if is_valid(choice):
            #return choice
        while True:
            try:
                choice = int(choice)
            except ValueError as error:
                print('enter a numeral !!')
            if choice not in (0,1,2,):
                choice = input('this choice is not a part of the proposals, try again ! ')

            else:
                break
        return choice

    def second_menu(self):

        Category.menu()
        print('To return: r')
        print('To quit : 0')
        categoryChoice = int(input())
        return self.listCategory[categoryChoice-1]