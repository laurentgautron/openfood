
class Product:

    @staticmethod
    def create():

        sql = """ CREATE TABLE IF NOT EXISTS product (
                    code BIGINT NOT NULL,
                    name VARCHAR(255),
                    nutri_score VARCHAR(1),
                    description TEXT(100),
                    link VARCHAR(255),
                    PRIMARY KEY(code))
                    ENGINE = INNODB; """
        return sql