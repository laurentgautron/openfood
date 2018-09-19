
from category import Category
from categoryProduct import CategoryProduct
from store import Store
from storeProduct import StoreProduct
from product import Product
from historic import Historic
from createtables import CreateTables

class Main:

    def openfood(self):

        category = Category.create()
        product = Product.create()
        store = Store.create()
        categoryProduct = CategoryProduct.create()
        storeProduct = StoreProduct.create()
        historic = Historic.create()
        lisTable = [category, product, store, categoryProduct, storeProduct, historic]
        CreateTables.creation(lisTable)


if __name__ == '__main__':
    main = Main()
    main.openfood()