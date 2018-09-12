import os
from createtables import Createtables
from getdatas import Getdatas
from insertdatas import Insertdatas

class Main:

    def __init__(self):

        self.creation = Createtables()
        self.datas = Getdatas()
        self.datastables = Insertdatas()
        
    def openfood(self):

        self.creation.create()
        if not os.path.isfile('openfoodbase.json'):
            self.categories = self.datas.find_categories()
            self.products = self.datas.find_products(self.categories)
            #self.datas.get_json(self.categories,'categories.json')
            self.datas.get_json(self.products,'openfoodbase.json')
             #self.datastables.category_product()


if __name__ == '__main__':
    main = Main()
    main.openfood() 