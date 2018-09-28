import mysql.connector
import os
from category import Category

class Menu:

    @staticmethod
    def make_choice(itemList=['categories','historic']):

        while True:
            choice = input('your choice is (enter a number beteween 1 and %d): '%len(itemList))
            try:
                choice = int(choice)
            except ValueError as error:
                print('enter a numeral !!')
            else:
                if not 0 <= choice < len(itemList)+1:
                    choice = input('this choice is not a part of the proposals, try again ! ')
                else:
                    break
        return itemList[choice-1]

    @staticmethod
    def display(itemList, nameList):

        os.system('clear')
        print('make your choice by choosing the corresponding number among the propositions !! ')
        print('To return: r')
        print('To quit : 0')
        print('------ %s ------'%nameList)
        for indice, value in enumerate(itemList):
            print(' %d -  %s'%(indice+1, value))