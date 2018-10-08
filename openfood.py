""" main program for the openfood application """
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
        """ create an instance of Datas and test if there is the openfoodbase.json file """
        self.find = os.path.isfile('openfoodbase.json')
        self.datas = Datas()
        
    def preparations(self):
        """ methods to make a json file, get datas, create tables and fill them """
        os.system('clear')
        print('get datas and create a json file...')
        self.datas.mkjsonfile()
        print('create and fille tables...')
        Tables.creation()
        Tables.fill_tables() 

    def use_openfood(self):
        """ display menu according user's choice and record his choice """
        choice = 'y'
        while choice == 'y':
            os.system('clear')
            Menu.display(['categories', 'historic'], 'Main menu')
            print('make your choice by choosing the corresponding number among the propositions !! ')
            choiceMenu = Menu.make_choice()
            if choiceMenu == 0:
                break
            elif choiceMenu == 'categories':
                categories = Category.get_datas()
                Menu.display(categories, 'Categories')
                choiceCategory = Menu.make_choice(categories)
                if choiceCategory == 0:
                    break
                else:
                    products = CategoryProduct.get_datas(choiceCategory)
                    Menu.display(products, 'Products')
                    choiceProduct = Menu.make_choice(products)
                    if choiceProduct == 0:
                        break
                    else:
                        details = Product.show_details(choiceProduct[1])
                        Menu.display(details, 'details product')
                        substitute = Product.propose_substitute(choiceCategory, choiceProduct[1])
                        if substitute != 0:
                            detailSubstitute = Product.show_details(substitute)
                            Menu.display(detailSubstitute, 'details substitute')
                            Historic.insert(substitute, choiceProduct[1])
            elif choiceMenu == 'historic':
                historics = Historic.get_datas()
                if historics:
                    for hist in historics:
                        detailProduct = Product.show_details(hist[0])
                        detailSubstitute = Product.show_details(hist[1])
                        Menu.display(detailProduct, 'details product')
                        Menu.display(detailSubstitute, 'details substitute')
                else:
                    print('You have no historic for the moment')
            choice = input('go to the Main menu ? (y/n)')
            while choice not in ('y', 'n'):
                print('choose \'y\' or \'n\'')

    def openfood(self):
        """ the main function """
        if not self.find:
            self.preparations()
        self.use_openfood()


if __name__ == '__main__':
    main = Main()
    main.openfood()
