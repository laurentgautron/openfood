import requests
import json

nbCategory = 20
nbProducts = 30

r_category = requests.get('https://fr.openfoodfacts.org/categories.json')
cat = r_category.json()
listCategory = []

for i in range(20):
    listCategory.append(cat['tags'][i]['name'])

dictCatProducts = {}

for category in listCategory:
    settings = {f"action":"process","tagtype_0":"categories","tag_contains_0":"contains","tag_0":{category},"sort_by":"unique_scans_n","page_size":{nbProducts},"json":1}
    r_products = requests.get('https://fr.openfoodfacts.org/cgi/search.pl?',params=settings)
    products = r_products.json()
    listProductsInfo = {}
    for i in range(nbProducts):
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

with open('openfooddatas.json','w') as f:
    json.dump(dictCatProducts,f, indent=4)