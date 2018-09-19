
from category import Category
from categoryProduct import CategoryProduct
from store import Store
from storeProduct import StoreProduct
from product import Product
from historic import Historic
from tables import Tables
from datas import Datas
import os

class Main:

    def __init__(self):

        self.category = Category.create()
        self.product = Product.create()
        self.store = Store.create()
        self.categoryProduct = CategoryProduct.create()
        self.storeProduct = StoreProduct.create()
        self.historic = Historic.create()
        self.empty = os.path.isfile('openfoodbase.json')
        self.datas = Datas()

    def openfood(self):

        if not self.empty:
            os.system('clear')
            Tables.remove()
            lisTable = [self.category, self.product, self.store, self.categoryProduct, self.storeProduct, self.historic]
            Tables.creation(lisTable)
            self.datas.mkjsonfile()


if __name__ == '__main__':
    main = Main()
    main.openfood()