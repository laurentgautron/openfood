from createtables import Createtables
from getdatas import Getdatas

class Main:

    def __init__(self):
        self.creation = Createtables()
        self.datas = Getdatas()

    def openfood(self):
        self.creation.create()
        self.categories = self.datas.find_categories()
        self.products = self.datas.find_products(self.categories)
        self.jsondatas = self.datas.get_json(self.products)

if __name__ == '__main__':
    main = Main()
    main.openfood() 