""" all opération cooresponding to a SQL code in historic table ."""
from connection import Connection

class Historic:
    """ class category contain all methods concernig historic table ."""
    @staticmethod
    def create():
        """ create histotic table ."""
        sql = """ CREATE TABLE IF NOT EXISTS historic (
                    code_to_substitute BIGINT(13) NOT NULL,
                    substitute_code BIGINT(13),
                    create_at DATETIME,
                    PRIMARY KEY (code_to_substitute))
                    ENGINE = INNODB; """
        with Connection.get_instance() as cursor:
            cursor.execute(sql)

    @staticmethod
    def insert(substitute, code):
        """ insert datas in table historic : product code to substitute and teh substitute code."""
        with Connection.get_instance() as cursor:
            sql = "SELECT count(code_to_substitute) FROM historic WHERE code_to_substitute = %s;"
            cursor.execute(sql, (code,))
            test = cursor.fetchone()
            if test[0] == 0:
                sql = """INSERT INTO historic (code_to_substitute, substitute_code, create_at)\
                         VALUES (%s, %s, NOW());"""
                cursor.execute(sql, (code, substitute))
            else:
                print('you\'ve already made a research for this food')

    @staticmethod
    def get_datas():
        """ recover datas from historic table in a list of tuple:
            (porduct code, substitute code) ."""
        with Connection.get_instance() as cursor:
            sql = """SELECT code_to_substitute, substitute_code FROM historic \
                     ORDER BY create_at DESC;"""
            cursor.execute(sql)
            code_substitute = cursor.fetchall()
        return code_substitute
