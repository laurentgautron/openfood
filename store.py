
class Store:

    @staticmethod
    def create():

        sql = """ CREATE TABLE IF NOT EXISTS store (
                    name VARCHAR(255) NOT NULL,
                    PRIMARY KEY(name))
                    ENGINE = INNODB; """
        return sql