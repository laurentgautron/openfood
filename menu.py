import os
import mysql.connector

class Menu:

    def __init__(self):

        self.howToExit = 'if you want exit the application enter 0 !'
        self.connection = mysql.connector.connect(host = 'localhost', user = 'lolo', password = 'cestmoi', database = 'openfoodbase')
        self.makechoice = 'make your choice by choosing the corresponding number among the propositions: '

    def first_menu(self):

        categoryChoice = int
        while categoryChoice not in [0,1,2]:
            try:
                os.system("clear")
                print(self.howToExit) 
                print('-------- Main menu --------')
                print('1 - : consult the categories')
                print('2 - : consult the history')
                categoryChoice = int(input(self.makechoice))
            except ValueError as e:
                continue
        return categoryChoice

    def next_menu(self,menuchoice):

        os.system("clear")
        print(self.howToExit)
        self.menuchoice = menuchoice
        print('------ %s ------'%self.menuchoice)
        sql = "SELECT name FROM %s"%self.menuchoice
        cursor = self.connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for number, category in enumerate(rows):
            print(' %d - : %s'%(number+1,category))
        return rows[int(input(self.makechoice))-1]
