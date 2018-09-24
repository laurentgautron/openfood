from tables import Tables
from datas import Datas
from menu import Menu
from categoryProduct import CategoryProduct
import os

class Main:

    def __init__(self):

        self.empty = os.path.isfile('openfoodbase.json')
        self.datas = Datas()
        self.menu = Menu()
        
    def openfood(self):

        if not self.empty:
            os.system('clear')
            Tables.remove()
            self.datas.mkjsonfile()
            Tables.creation()
            Tables.fill_tables()
        choice = self.menu.first_menu()
        #while choice != 'q':
        if choice == 1:
            categoryChoice = self.menu.second_menu()
            CategoryProduct.menu(categoryChoice)

        #else:
            #choiceTwo = self.menu.second_menu(choiceOne, historic )



if __name__ == '__main__':
    main = Main()
    main.openfood()