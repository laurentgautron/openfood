import os

class Menu:

    def first_menu(self):

        choice = int()
        while choice not in [1,2,3]:
            try:
                os.system("clear") 
                print('-------- menu pricipal --------')
                print('1 - : consult the catégories')
                print('2 - : consult the history')
                print('3 - : exit')
                choice = int(input('make your choice by choosing the corresponding number among the propositions: '))
            except ValueError as e:
                continue
        if choice == 3:
            return 0
        else:
            return choice