from createtables import Createtables
from getdatas import Getdatas
#from insertdatas import Insertdatas

class Main:

    def __init__(self):
        self.creation = Createtables()
        self.datas = Getdatas()
        #self.insertDatas = Insertdatas('openfoodbase')

    def openfood(self):
        self.creation.create()
        self.categories = self.datas.find_categories()
        self.datas.get_json(self.categories,'categories.json')
        self.products = self.datas.find_products(self.categories)
        self.datas.get_json(self.products,'openfoodbase.json')
        #self.insertdatas.insert_openfood_datas()


if __name__ == '__main__':
    main = Main()
    main.openfood() 