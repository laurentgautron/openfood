from createtables import Createtables
from getdatas import Getdatas

class Main:

    def __init__(self):
        self.creation = Createtables()
        self.datas = Getdatas()

    def openfood(self):
        self.creation.create()
        self.categories = self.datas.find_categories()
        self.jsonCategoriesDatas = self.datas.get_json(self.categories,'categories.json')
        self.products = self.datas.find_products(self.categories)
        self.jsonProductsDatas = self.datas.get_json(self.products,'openfoodbase.json')

if __name__ == '__main__':
    main = Main()
    main.openfood() 