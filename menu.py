""" treat the menu choice and display menu list """
import os

class Menu:
    """ contain two static methods : make_a_choice and display """
    @staticmethod
    def make_choice(itemList=['categories', 'historic']):
        """ return the menu choice after testing if choice is an integer """
        print('to quit :(0)')
        while True:
            try:
                choice = int(input('your choice is (enter a number beteween 1 and %d): '%len(itemList)))
            except ValueError as error:
                print('enter a numeral !!')
                continue
            else:
                if not 0 <= choice < len(itemList)+1:
                    print('this choice is not a part of the proposals, try again ! ')
                    continue
                else:
                    break
        if choice == 0:
            return choice
        else:
            return itemList[choice-1]

    @staticmethod
    def display(itemList, nameList):
        """ dispaly the menu according to the list in settings """
        if nameList not in ('details product', 'details substitute'):
            os.system('clear')
        if nameList == 'historics':
            for val in itemList:
                print('--- Userchoice :%s ------ Substitute : %s' %(val[0],values[1]))
        else:
            print('------ %s ------'%nameList)
            for indice, value in enumerate(itemList):
                if nameList == 'Main menu':
                    print(' %d -  %s'%(indice+1, value))
                elif nameList in ('details product', 'details substitute'):
                    print(' -  %s'%value)
                else:
                    print(' %d -  %s'%(indice+1, value[0]))
