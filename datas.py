import requests
import json

class Datas:

    NBCATEGORIES = 20
    NBPRODUCTS = 30

    def get_category(self,nbcat):

        url_category = 'https://fr.openfoodfacts.org/categories.json'
        r_category = requests.get(url_category)
        cat_json = r_category.json()
        listCategories = []
        for item in range(nbcat):
            cat = cat_json['tags'][item]['name'], cat_json['tags'][item]['url'].split('/')[-1]
            listCategories.append(cat)
        return listCategories

    def get_all_datas(self,category, products):

        dict_datas = {}
        for product in products:
            dict_datas[category[0]] = products
        return dict_datas

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
                listInfoProduct[code]['store'] = product_json['products'][item]['stores']
                listInfoProduct[code]['description'] = product_json['products'][item]['generic_name_fr']
                listInfoProduct[code]['link'] = product_json['products'][item]['url']
                listInfoProduct[code]['nutri_score'] = product_json['products'][item]['nutrition_grade_fr']
            except KeyError as error:
                continue
        return listInfoProduct

    def record_datas(self, nbCategory, nbProduct):

        self.nbCategory = nbCategory
        self.nbProduct = nbProduct
        categories = self.get_category(nbCategory)
        print(categories)
        for category in categories:
            products = self.get_product(category, nbProduct)
            dict_datas_product = self.get_all_datas(category, products)
            print(dict_datas_product)
        return dict_datas_product

    def mkjsonfile(self):

        dict_to_json = self.record_datas(self.NBCATEGORIES, self.NBPRODUCTS)
        with open('openfoodbase.json', 'w') as jsonfile:
            json.dump(dict_to_json, jsonfile, indent=4)