

-- 3. Сравнить цену каждого продукта n с средней ценой продуктов
--      в категории продукта n. Использовать window function.
--    Таблица результата должна содержать такие колонки:
--      category_title, product_title, price, avg.

CREATE OR REPLACE
    FUNCTION products_with_price_and_avg_price()
    RETURNS TABLE
            (
                category_title varchar,
                product_title  varchar,
                price          float,
                avg            float
            )
    LANGUAGE plpgsql
AS
$$
BEGIN
    RETURN QUERY
        SELECT categories.category_title,
               products.product_title,
               products.price,
               AVG(products.price)
               OVER (PARTITION BY products.category_id) AS avg
        FROM products
                 JOIN categories USING (category_id);
END;
$$;

SELECT products_with_price_and_avg_price.*
FROM products_with_price_and_avg_price();
