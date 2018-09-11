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
            category = (cat['tags'][i]['name'],cat['tags'][i]['url'].split('/')[-1])
            self.listCategories.append(category)
        return self.listCategories

    def find_products(self, categories):

        dicDataProducts = {}
        for category in categories:
            settings = {"action":"process","tagtype_0":"categories","tag_contains_0":"contains","tag_0":category[1],"sort_by":"unique_scans_n","page_size":str(self.NBPRODUCTS),"json":1}
            r_products = requests.get(self.urlProducts,params=settings)
            products = r_products.json()
            listProductsInfo = {}
            for i in range(self.NBPRODUCTS):
                code = products["products"][i]["code"]
                listProductsInfo[code] = {'name':'','description':'','link':'','store':'','nutriScore':''}
                try:
                    listProductsInfo[code]['name'] = products["products"][i]["product_name"]
                    listProductsInfo[code]['description'] = products["products"][i]["generic_name_fr"]
                    listProductsInfo[code]['link'] = products["products"][i]["url"]
                    listProductsInfo[code]['store'] = products["products"][i]["stores"]
                    listProductsInfo[code]['nutriScore'] = products["products"][i]["nutrition_grade_fr"]
                except Exception as e:
                    continue
            dicDataProducts[category[0]] =  listProductsInfo
        return dicDataProducts

    def get_json(self, dictDatas, file):
        with open(file,'w') as f:
            json.dump(dictDatas,f, indent=4)