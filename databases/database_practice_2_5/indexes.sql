-- Придумать 3 запроса, которые можно оптимизировать с помощью индекса (проверять
-- стоит ли оптимизировать запрос оператором explain) и оптимизировать их
-- используя индекс. Результат проверять также оператором explain.

EXPLAIN ANALYZE
SELECT products.*
FROM products
WHERE product_title
LIKE '%2%';

CREATE INDEX products_product_title_idx ON products (product_title);

DROP INDEX products_product_title_idx;



EXPLAIN ANALYZE
SELECT potential_customers.*
FROM potential_customers
WHERE surname LIKE '%A%';

CREATE INDEX potential_customers_surname_idx
ON potential_customers (surname);

DROP INDEX potential_customers_surname_idx;



EXPLAIN ANALYZE
SELECT carts.*
FROM carts
         INNER JOIN users
                    ON users.user_id = carts.users_user_id
WHERE users.user_id = 10
ORDER BY users.first_name;

CREATE INDEX users_user_id_first_name_idx ON users (user_id, first_name);

CREATE INDEX carts_users_user_id_idx ON carts (users_user_id);

DROP INDEX users_user_id_first_name_idx;

DROP INDEX carts_users_user_id_idx;


EXPLAIN ANALYZE
SELECT products.*
from products
         INNER JOIN categories
             USING(category_id)
WHERE category_id >  50
ORDER BY category_id;

CREATE INDEX categories_category_id_idx ON categories (category_id);

CREATE INDEX products_category_id_idx ON products (category_id);

DROP INDEX categories_category_id_idx;

DROP INDEX products_category_id_idx;
