from tables import Tables
from datas import Datas
from menu import Menu
from categoryProduct import CategoryProduct
from category import Category
from connection import Connection
from historic import Historic
from product import Product
import os

class Main:

    def __init__(self):

        self.find = os.path.isfile('openfoodbase.json')
        self.datas = Datas()
        self.conn = Connection()
        
    def preparations(self, db):

        os.system('clear')
        print('get datas and create a json file...')
        self.datas.mkjsonfile()
        print('create and fille tables...')
        Tables.creation(db)
        Tables.fill_tables(db)
        

    def use_openfood(self, db):

        choice = 'a'
        while choice != 'q':
            Menu.display(['categories', 'historic'],'Main menu')
            choice = Menu.make_choice()
            if choice == 'categories':
                categories = Category.get_datas(db)
                Menu.display(categories, 'Categories')
                choiceCategory = Menu.make_choice(categories)
                products = CategoryProduct.get_datas(db, choiceCategory)
                Menu.display(products, 'Products')
                choiceProduct = Menu.make_choice(products)
                details = Product.show_details(db, choiceProduct[1])
                Menu.display(details, 'details')
                substitute = Product.propose_substitute(db, choiceCategory, choiceProduct[1])
                Menu.display(substitute, 'details substitute')
                Historic.insert(db, substitute[0], choiceProduct[1])
            elif choice == 'historics':
                historics = Historic.get_datas(db)
                print(historics)
                input()
                Menu.display(historics, 'historics')
                

    def openfood(self):

        with self.conn as db:
            if not self.find:
                self.preparations(db)
            self.use_openfood(db)


if __name__ == '__main__':
    main = Main()
    main.openfood()