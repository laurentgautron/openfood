
import json
import requests


class Getdatas:

    NBCATEGORIES = 20
    NBPRODUCTS = 30

    def __init__(self):

        self.url_categories = 'https://fr.openfoodfacts.org/categories.json'
        self.url_products = 'https://fr.openfoodfacts.org/cgi/search.pl?'

    def find_categories(self):

        r_categories = requests.get(self.url_categories)
        cat = r_categories.json()
        self.list_categories = []
        for item in range(self.NBCATEGORIES):
            category = (cat['tags'][item]['name'], cat['tags'][item]['url'].split('/')[-1])
            self.list_categories.append(category)
        return self.list_categories

    def fill_product_table(self, products, nb_products):

        list_products_info = {}
        for item in range(self.NBPRODUCTS):
            code = products["products"][item]["code"]
            list_products_info[code] = {'name':'', 'description':'', 'link':'', 'store':'', 'nutri_score':''}
            try:
                list_products_info[code]['name'] = products["products"][itel]["product_name"]
                list_products_info[code]['description'] = products["products"][item]["generic_name_fr"]
                list_products_info[code]['link'] = products["products"][item]["url"]
                list_products_info[code]['store'] = products["products"][item]["stores"]
                list_products_info[code]['nutri_score'] = products["products"][item]["nutrition_grade_fr"]
            except KeyError as error:
                del list_products_info[code]
                continue
            if list_products_info[code]['store'] == "":
                del list_products_info[code]
        return list_products_info

    def find_products(self, categories):

        dic_data_products = {}
        for category in categories:
            settings = {"action":"process", "tagtype_0":"categories", "tag_contains_0":"contains", "tag_0":category[1],\
                        "sort_by":"unique_scans_n", "page_size":str(self.NBPRODUCTS), "json":1}
            r_products = requests.get(self.url_products, params=settings)
            products = r_products.json()
            dic_data_products[category[0]] = self.fill_product_table(products, self.NBPRODUCTS)
        return dic_data_products

    def get_json(self, dict_datas, file):
        with open(file, 'w') as f:
            json.dump(dictDatas, f, indent=4)

    