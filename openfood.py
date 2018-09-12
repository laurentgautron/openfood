import os
from createtables import Createtables
from getdatas import Getdatas
from operationonbase import Operationonbase

class Main:

    def __init__(self):

        self.creation = Createtables()
        self.datas = Getdatas()
        self.operationonbase = Operationonbase()
        
    def openfood(self):

        if not os.path.isfile('openfoodbase.json'):
            self.operationonbase.remove()
            self.categories = self.datas.find_categories()
            self.products = self.datas.find_products(self.categories)
            self.datas.get_json(self.products,'openfoodbase.json')
        self.creation.create()
        self.operationonbase.datas_in_tables()


if __name__ == '__main__':
    main = Main()
    main.openfood() 