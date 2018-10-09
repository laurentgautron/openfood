""" main program for the openfood application ."""
import os
from tables import Tables
from datas import Datas
from menu import Menu
from categoryproduct import CategoryProduct
from category import Category
from historic import Historic
from product import Product

class Main:

    def __init__(self):
        """ create an instance of Datas and test if there is the openfoodbase.json file ."""
        self.find = os.path.isfile('openfoodbase.json')
        self.datas = Datas()

    def preparations(self):
        """ methods to make a json file, get datas, create tables and fill them ."""
        os.system('clear')
        print('get datas and create a json file...')
        self.datas.mkjsonfile()
        print('create and fille tables...')
        Tables.creation()
        Tables.fill_tables()

    @staticmethod
    def use_openfood():
        """ display menu according user's choice and record his choice ."""
        choice = 'y'
        while choice == 'y':
            os.system('clear')
            Menu.display(['categories', 'historic'], 'Main menu')
            print('make your choice by choosing the corresponding number among the propositions!!')
            choice_menu = Menu.make_choice()
            if choice_menu == 0:
                break
            elif choice_menu == 'categories':
                categories = Category.get_datas()
                Menu.display(categories, 'Categories')
                choice_category = Menu.make_choice(categories)
                if choice_category == 0:
                    break
                else:
                    products = CategoryProduct.get_datas(choice_category)
                    Menu.display(products, 'Products')
                    choice_product = Menu.make_choice(products)
                    if choice_product == 0:
                        break
                    else:
                        details = Product.show_details(choice_product[1])
                        Menu.display(details, 'details product')
                        substitute = Product.propose_substitute(choice_category, choice_product[1])
                        if substitute != 0:
                            detail_substitute = Product.show_details(substitute)
                            Menu.display(detail_substitute, 'details substitute')
                            Historic.insert(substitute, choice_product[1])
            elif choice_menu == 'historic':
                historics = Historic.get_datas()
                if historics:
                    for hist in historics:
                        detail_product = Product.show_details(hist[0])
                        detail_substitute = Product.show_details(hist[1])
                        print()
                        Menu.display(detail_product, 'details product')
                        print()
                        Menu.display(detail_substitute, 'details substitute')
                        user_choice = '\n'
                        while user_choice == '\n':
                            user_choice = input('press ENTER to continue ! or (q) to quit !')
                        print('no other datas !')
                        if user_choice == 'q':
                            break
                        else:
                            continue
                else:
                    print('You have no historic for the moment')
            choice = input('go to the Main menu ? (y/n)')
            while choice not in ('y', 'n'):
                choice = input('choose \'y\' or \'n\'')

    def openfood(self):
        """ the main function ."""
        if not self.find:
            self.preparations()
        Main.use_openfood()


if __name__ == '__main__':
    main = Main()
    main.openfood()
