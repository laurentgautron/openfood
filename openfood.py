from tables import Tables
from datas import Datas
from menu import Menu
from categoryProduct import CategoryProduct
from category import Category
from historic import Historic
from product import Product
import os

class Main:

    def __init__(self):

        self.find = os.path.isfile('openfoodbase.json')
        self.datas = Datas()
        
    def preparations(self):

        os.system('clear')
        print('get datas and create a json file...')
        self.datas.mkjsonfile()
        print('create and fille tables...')
        Tables.creation()
        Tables.fill_tables()
        

    def use_openfood(self):

        os.system('clear')
        choice = 'y'
        while choice == 'y':
            Menu.display(['categories', 'historic'],'Main menu')
            print('make your choice by choosing the corresponding number among the propositions !! ')
            choiceMenu = Menu.make_choice()
            if choice == 0:
                break
            if choiceMenu == 'categories':
                categories = Category.get_datas()
                Menu.display(categories, 'Categories')
                choiceCategory = Menu.make_choice(categories)
                products = CategoryProduct.get_datas(choiceCategory)
                Menu.display(products, 'Products')
                choiceProduct = Menu.make_choice(products)
                details = Product.show_details(choiceProduct[1])
                print('details for product: ')
                Menu.display(details, 'details')
                substitute = Product.propose_substitute(choiceCategory, choiceProduct[1])
                if substitute !=0:
                    print('details for substitute')
                    detailSubstitute = Product.show_details(substitute)
                    Menu.display(detailSubstitute, 'details substitute')
                    Historic.insert(substitute, choiceProduct[1])
            else:
                historics = Historic.get_datas()
                Menu.display(historics, 'historics')
                if historics == []:
                    print('You have no historic for the moment')
            choice= input('Do you want redo a choice ? (y/n)')
            while choice not in ('y', 'n'):
                choice = input('choose (Y)es or (N)o : ')
                

                

    def openfood(self):

        #self.config = {'host':'localhost','user':'','password':''}
        #nom = input('entrer your user name: ')
        #password = input('enter your password: ')
        #self.config['user'] = nom
        #self.config['password'] = password
        if not self.find:
            self.preparations()
        self.use_openfood()


if __name__ == '__main__':
    main = Main()
    main.openfood()