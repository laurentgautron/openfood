""" the finality of this module is to make a json file with the openfoodfacts datas """
import json
import requests

class Datas:

    def __init__(self):
        """ to fix nb categories and nb product by categories to extract """
        self.nbCategories = 20
        self.nbProduct = 30

    def is_empty(self, lisToTest):
        """ test if values for a key is empty"""
        test = False
        for key in lisToTest.keys():
            item = ''.join(lisToTest[key])
            item = item.replace(' ','')
            if item == '':
                test = True
        return test

    def filter(self, stores):
        """  to filter stores: removes spaces and upper case"""
        stores = list(stores.split(','))
        lisToFilter = []
        for store in stores:
            if store not in lisToFilter:
                store = store.strip()
                store = store.lower()
                lisToFilter.append(store)
        return list(set(lisToFilter))

    def get_category(self, nbcat):
        """ make a list for  the first 20 categories """
        url_category = 'https://fr.openfoodfacts.org/categories.json'
        rCategory = requests.get(url_category).json()
        #cat_json = r_category.json()
        listCategories = []
        for item in range(nbcat):
            cat = rCategory['tags'][item]['name'], rCategory['tags'][item]['url'].split('/')[-1]
            listCategories.append(cat)
        return listCategories

    def get_product(self,category, nbProduct):
        """ create a dictionnary with details for the first 30 product of a category """
        url_product = 'https://fr.openfoodfacts.org/cgi/search.pl?'
        setting = {"action":"process", "tagtype_0":"categories", "tag_contains_0":"contains", "tag_0":category[1],\
                    "sort_by":"unique_scans_n","page_size":nbProduct,"json":1}
        r_product = requests.get(url_product, setting)
        product_json = r_product.json()
        listInfoProduct = {}
        for item in range(nbProduct):
            code = product_json['products'][item]['code']
            listInfoProduct[code] = {'name':' ', 'store':' ', 'description':' ', 'link':' ', 'nutri_score':' '}
            try:
                listInfoProduct[code]['name'] = product_json['products'][item]['product_name']
                listInfoProduct[code]['store'] = self.filter(product_json['products'][item]['stores'])
                listInfoProduct[code]['description'] = product_json['products'][item]['generic_name_fr']
                listInfoProduct[code]['link'] = product_json['products'][item]['url']
                listInfoProduct[code]['nutri_score'] = product_json['products'][item]['nutrition_grade_fr']
            except KeyError as error:
                del listInfoProduct[code]
                continue
            if self.is_empty(listInfoProduct[code]):
                del listInfoProduct[code]
        return listInfoProduct

    def record_datas(self, nbCategory, nbProduct):
        """ make a big dictionnary with categories and products"""
        dict_datas_product = {}
        categories = self.get_category(nbCategory)
        for category in categories:
            dict_datas_product[category[0]] = self.get_product(category, nbProduct)
        return dict_datas_product

    def mkjsonfile(self):
        """ make the json file """
        dict_to_json = self.record_datas(self.nbCategories, self.nbProduct)
        with open('openfoodbase.json', 'w') as jsonfile:
            json.dump(dict_to_json, jsonfile, indent=4)
