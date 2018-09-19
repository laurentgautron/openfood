
class CategoryProduct:

    @staticmethod
    def create():

        sql = """ CREATE TABLE IF NOT EXISTS category_product (
                            category_name VARCHAR(100),
                            product_code BIGINT,
                            PRIMARY KEY (category_name,product_code),
                            CONSTRAINT `fk_category_product_category` FOREIGN KEY (`category_name`) REFERENCES `category`(`name`),
                            CONSTRAINT `fk_category_product_product` FOREIGN KEY (`product_code`) REFERENCES `product`(`code`))
                            ENGINE = INNODB;
                        """
        return sql
