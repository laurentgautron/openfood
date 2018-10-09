""" the finality of this module is to make a json file with the openfoodfacts datas ."""
import json
import requests

class Datas:

    def __init__(self):
        """ to fix nb categories and nb product by categories to extract ."""
        self.nb_categories = 20
        self.nb_product = 30

    @staticmethod
    def is_empty(list_to_test):
        """ test if values for a key is empty in a dictionnary
            return a boolean.
        """
        test = False
        for key in list_to_test.keys():
            item = ''.join(list_to_test[key])
            item = item.replace(' ', '')
            if item == '':
                test = True
        return test

    @staticmethod
    def filter(stores):
        """  to filter stores: removes spaces and upper case
             store is the list of store to filter
             return a filtered list.
        """
        stores = list(stores.split(','))
        list_to_filter = []
        for store in stores:
            if store not in list_to_filter:
                store = store.strip()
                store = store.lower()
                list_to_filter.append(store)
        return list(set(list_to_filter))

    @staticmethod
    def get_category(nbcat):
        """ make a list for the first 20 categories
            return a list of tuples : (the category name, the category name for a request).
        """
        url_category = 'https://fr.openfoodfacts.org/categories.json'
        r_category = requests.get(url_category).json()
        #cat_json = r_category.json()
        list_categories = []
        for item in range(nbcat):
            #cat his tehe category name without spases, qotations marks : for the url request
            cat = r_category['tags'][item]['name'], r_category['tags'][item]['url'].split('/')[-1]
            list_categories.append(cat)
        return list_categories

    @staticmethod
    def get_product(category, nb_product):
        """ create a dictionnary with details for the first 30 product code of a category ."""
        url_product = 'https://fr.openfoodfacts.org/cgi/search.pl?'
        setting = {"action":"process", "tagtype_0":"categories", "tag_contains_0":"contains", "tag_0":category[1],\
                    "sort_by":"unique_scans_n", "page_size":nb_product, "json":1}
        r_product = requests.get(url_product, setting)
        product_json = r_product.json()
        list_inf_product = {}
        for item in range(nb_product):
            code = product_json['products'][item]['code']
            list_inf_product[code] = {'name':' ', 'store':' ', 'description':' ', 'link':' ', 'nutri_score':' '}
            try:
                list_inf_product[code]['name'] = product_json['products'][item]['product_name']
                list_inf_product[code]['store'] = Datas.filter(product_json['products'][item]['stores'])
                list_inf_product[code]['description'] = product_json['products'][item]['generic_name_fr']
                list_inf_product[code]['link'] = product_json['products'][item]['url']
                list_inf_product[code]['nutri_score'] = product_json['products'][item]['nutrition_grade_fr']
            except KeyError as error:
                del list_inf_product[code]
                continue
            if Datas.is_empty(list_inf_product[code]):
                del list_inf_product[code]
        return list_inf_product

    @staticmethod
    def record_datas(nb_category, nb_product):
        """ make a big dictionnary with categories and products ."""
        dict_datas_product = {}
        categories = Datas.get_category(nb_category)
        for category in categories:
            dict_datas_product[category[0]] = Datas.get_product(category, nb_product)
        return dict_datas_product

    def mkjsonfile(self):
        """ make the json file ."""
        dict_to_json = Datas.record_datas(self.nb_categories, self.nb_product)
        with open('openfoodbase.json', 'w') as json_file:
            json.dump(dict_to_json, json_file, indent=4)
