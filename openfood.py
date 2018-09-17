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
        self.operation_on_base = Operationonbase()
        self.remove = Remove()
        

    def openfood(self):

        empty = not os.path.isfile('openfoodbase.json')
        if empty:
            self.remove.remove_the_base()
            self.categories = self.datas.find_categories()
            self.products = self.datas.find_products(self.categories)
            self.datas.get_json(self.products, 'openfoodbase.json')
        self.creation.create()
        self.operation_on_base.datas_in_tables()
        self.menu = Menu()
        choice = self.menu.first_menu()
        print(choice)
        while choice != 0:
            if choice == 1:
                category_choice = self.menu.next_menu('category')
                product_choice = self.menu.next_menu(category_choice)


if __name__ == '__main__':
    main = Main()
    main.openfood() 