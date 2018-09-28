import json
import mysql.connector

class Historic:

    @staticmethod
    def create(db):

        sql = """ CREATE TABLE IF NOT EXISTS historic (
                    code_to_substitute BIGINT NOT NULL,
                    substitute_code BIGINT,
                    PRIMARY KEY (code_to_substitute))
                    ENGINE = INNODB; """
        db.execute(sql)

    @staticmethod
    def insert(db, substitute, code):

        with open('openfoodbase.json', 'r') as f:
            datasopenfood = json.load(f)
        sql = """INSERT INTO historic (code_to_substitute, substitute_code) VALUES (%s, %s);"""
        db.execute(sql, (code, substitute))

    @staticmethod
    def get_datas(db):

        sql = """ SELECT * FROM historic;"""
        db.execute(sql)
        codes = db.fetchall()
        for line in codes:
            sqlProduct = """SELECT * FROM product
                            JOIN historic ON code = %s;"""
            db.execute(sql, line[0])
            product = db.fetchone()
            db.execute(sql, linee[1])
            substitute = db.fetchone()

