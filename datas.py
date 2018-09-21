import requests
import json
import mysql.connector

class Datas:

    def __init__(self):

        self.nbCategories = 20
        self.nbProduct = 30

    def filter(self, stores):
        
        stores = list(stores.split(','))
        lisToFilter = []
        for store in stores:
            if store not in lisToFilter:
                store = store.strip()
                store = store.lower()
                lisToFilter.append(store)
        return list(set(lisToFilter))

    def get_category(self,nbcat):

        url_category = 'https://fr.openfoodfacts.org/categories.json'
        r_category = requests.get(url_category)
        cat_json = r_category.json()
        listCategories = []
        for item in range(nbcat):
            cat = cat_json['tags'][item]['name'], cat_json['tags'][item]['url'].split('/')[-1]
            listCategories.append(cat)
        return listCategories

    def get_product(self,category, nbProduct):

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
                continue
            if product_json['products'][item]['stores'] == "":
                del listInfoProduct[code]
        return listInfoProduct

    def record_datas(self, nbCategory, nbProduct):

        dict_datas_product = {}
        categories = self.get_category(nbCategory)
        for category in categories:
            dict_datas_product[category[0]] = self.get_product(category, nbProduct)
        return dict_datas_product

    def mkjsonfile(self):

        dict_to_json = self.record_datas(self.nbCategories, self.nbProduct)
        with open('openfoodbase.json', 'w') as jsonfile:
            json.dump(dict_to_json, jsonfile, indent=4)