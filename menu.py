""" treat the menu choice and display menu list ."""
import os

class Menu:
    """ contain two static methods : make_a_choice and display ."""
    @staticmethod
    def make_choice(item_list=None):
        """ return the menu choice after testing if choice is an integer ."""
        if item_list is None:
            item_list = ['categories', 'historic']
        print('to quit :(0)')
        while True:
            try:
                choice = int(input('your choice is (enter a number beteween 1 and %d): '%len(item_list)))
            except ValueError as error:
                print('enter a numeral !!')
                continue
            else:
                if not 0 <= choice < len(item_list)+1:
                    print('this choice is not a part of the proposals, try again ! ')
                    continue
                else:
                    break
        if choice == 0:
            return choice
        else:
            return item_list[choice-1]

    @staticmethod
    def display(item_list, name_list):
        """ dispaly the menu according to the list in settings ."""
        if name_list not in ('details product', 'details substitute'):
            os.system('clear')
        if name_list == 'historics':
            for val in item_list:
                print('--- Userchoice :%s ------ Substitute : %s' %(val[0], val[1]))
        else:
            print('------ %s ------'%name_list)
            if name_list == 'Main menu':
                for indice, value in enumerate(item_list):
                    print(' %d -  %s'%(indice+1, value))
            elif name_list in ('details product', 'details substitute'):
                for key,value in item_list.items():
                    print(key,' - ',value)
            else:
                for indice, value in enumerate(item_list):
                    print(' %d -  %s'%(indice+1, value[0]))
