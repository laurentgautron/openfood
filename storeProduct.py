
class StoreProduct:

    @staticmethod
    def create():

        sql = """ CREATE TABLE IF NOT EXISTS store_product (
                    name_store VARCHAR(25),
                    code_pro_store BIGINT,
                    PRIMARY KEY (name_store, code_pro_store),
                    CONSTRAINT `fk_store_product_name` FOREIGN KEY (`name_store`) REFERENCES `store`(`name`),
                    CONSTRAINT `fk_store_product_code` FOREIGN KEY (`code_pro_store`) REFERENCES `product`(`code`))
                     ENGINE = INNODB; """
        return sql