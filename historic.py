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
        sqluse = """ USE openfoodbase;"""
        db.execute(sqluse)
        db.execute(sql)

    @staticmethod
    def insert(db, substitute, code):

        sql = "SELECT count(code_to_substitute) FROM historic WHERE code_to_substitute = %s;"
        db.execute(sql, (code,))
        test = db.fetchone()
        if test[0]==0:
            sql = """INSERT INTO historic (code_to_substitute, substitute_code) VALUES (%s, %s);"""
            db.execute(sql, (code, substitute))
        else:
            print('you\'ve already made a research for this food')

    @staticmethod
    def get_datas(db):

        sql = """SELECT prod1.name AS userchoice, prod2.name AS substitute \
                FROM historic JOIN product prod1 ON prod1.code = code_to_substitute \
                JOIN product prod2 ON prod2.code = substitute_code;"""
        db.execute(sql)
        codeSubstitute = db.fetchall()
        return codeSubstitute

