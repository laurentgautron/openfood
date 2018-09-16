import os
from createtables import Createtables
from getdatas import Getdatas
from operationonbase import Operationonbase
from removebase import Remove
from menu import Menu

class Main:

    def __init__(self):

        self.creation = Createtables()
        self.datas = Getdatas()
        self.operationonbase = Operationonbase()
        self.remove = Remove()
        self.menu = Menu()
        
    def openfood(self):

        empty = not os.path.isfile('openfoodbase.json')
        if empty:
            self.remove.remove_the_base()
            self.categories = self.datas.find_categories()
            self.products = self.datas.find_products(self.categories)
            self.datas.get_json(self.products,'openfoodbase.json')
            self.creation.create()
            self.operationonbase.datas_in_tables()
        choice  = self.menu.first_menu()
        print(choice)



if __name__ == '__main__':
    main = Main()
    main.openfood() 