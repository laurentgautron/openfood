import requests
import json

class Getdatas:

    NBCATEGORIES = 20
    NBPRODUCTS = 30

    def __init__(self):

        self.urlCategories = 'https://fr.openfoodfacts.org/categories.json'
        self.urlProducts = 'https://fr.openfoodfacts.org/cgi/search.pl?'

    def find_categories(self):

        r_categories = requests.get(self.urlCategories)
        cat = r_categories.json()
        self.listCategories = []
        for i in range(self.NBCATEGORIES):
            self.listCategories.append(cat['tags'][i]['name'])
        return self.listCategories

    def find_products(self, categories):

        dictCatProducts = {}
        for category in categories:
            settings = {f"action":"process","tagtype_0":"categories","tag_contains_0":"contains","tag_0":{category},"sort_by":"unique_scans_n","page_size":{self.NBPRODUCTS},"json":1}
            r_products = requests.get(self.urlProducts,params=settings)
            products = r_products.json()
            listProductsInfo = {}
            for i in range(self.NBPRODUCTS):
                print(i)
                try:
                    code = products["products"][i]["code"]
                    name = products["products"][i]["product_name"]
                    description = products["products"][i]["generic_name_fr"]
                    link = products["products"][i]["url"]
                    store = products["products"][i]["stores"]
                    nutriScore = products["products"][i]["nutrition_grade_fr"]
                    listProductsInfo[code] = [name,description,link,store,nutriScore]
                except Exception as e:
                    continue
                else:
                    dictCatProducts[category] = listProductsInfo
        return dictCatProducts

    def get_json(self, dictCatProducts):
        with open('openfooddatas.json','w') as f:
            json.dump(dictCatProducts,f, indent=4)