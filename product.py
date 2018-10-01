import json
import mysql.connector

class Product:

    @staticmethod
    def create(db):

        sql = """ CREATE TABLE IF NOT EXISTS product (
                    code BIGINT NOT NULL,
                    name VARCHAR(255),
                    nutri_score VARCHAR(1),
                    description TEXT(100),
                    link VARCHAR(255),
                    store VARCHAR(255),
                    PRIMARY KEY(code))
                    ENGINE = INNODB; """
        db.execute(sql)

    @staticmethod
    def insert(db):

        with open('openfoodbase.json', 'r') as f:
            datasopenfood = json.load(f)
        listCodes = []
        for datas in datasopenfood.values():
            for code, values in datas.items():
                if code not in listCodes:
                    listCodes.append(code)
                    code = int(code)
                    datasProduct = (code,values['name'], values['nutri_score'],values['link'], values['description'])
                    sql = """INSERT INTO product(code, name, nutri_score, link, description)
                            VALUES (%s, %s, %s, %s, %s);"""
                    db.execute(sql, datasProduct)

    @staticmethod
    def propose_substitute(db, choiceCategory, code):

        sqlresearch = """SELECT code, nutri_score FROM product 
                   JOIN category_product ON code = product_code
                   JOIN category ON category.id = category_id
                   WHERE category.name = %s AND product.nutri_score < (SELECT nutri_score FROM product WHERE code = %s);"""
        db.execute(sqlresearch, (choiceCategory[0], code))
        result = db.fetchall()
        if len(result) > 0:
            bestScore = 'e'
            place = 0
            indice = 0
            while (indice < len(result)) and (bestScore != 'a'):
                if result[indice][1] < bestScore:
                    bestScore = result[indice][1]
                    place = indice
                indice += 1
            sqlsubstitute = """SELECT * FROM product WHERE code = %s;"""
            db.execute(sqlsubstitute, (result[place][0],))
            substitute = db.fetchone()
            return substitute
        else:
            print('il n\'y a pas de substitut possible pour cet aliment')
            return 0

    @staticmethod
    def show_details(db, choiceProduct):

        sql = """SELECT * FROM product WHERE code = %s;"""
        db.execute(sql, (choiceProduct,))
        details = db.fetchone()
        return details