
class Historic:

    @staticmethod
    def create():

        sql = """ CREATE TABLE IF NOT EXISTS historic (
                    code_to_substitute BIGINT NOT NULL,
                    substitute_name VARCHAR(255),
                    PRIMARY KEY (code_to_substitute))
                    ENGINE = INNODB; """
        return sql