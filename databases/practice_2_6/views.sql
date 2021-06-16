-- Написать представление для таблицы products, для таблиц order_status и order, для таблиц products и category.
-- Создать материализированное представление для "тяжелого" запроса на свое усмотрение.
-- Не забыть сделать запросы для удаления представлений.


CREATE MATERIALIZED VIEW users_with_cart_average_bill
AS
SELECT user_id,
       CONCAT(first_name, ' ', last_name) AS name,
       count,
       avg_bill
FROM users
         JOIN (SELECT carts.users_user_id  AS id,
                      count(carts.cart_id) AS count,
                      avg(orders.total)    AS avg_bill
               FROM carts
                        JOIN orders ON carts.cart_id = orders.carts_cart_id
               GROUP BY users_user_id) AS bill
              ON users.user_id = bill.id
ORDER BY avg_bill DESC;

SELECT users_with_cart_average_bill.*
FROM users_with_cart_average_bill;

DROP MATERIALIZED VIEW users_with_cart_average_bill;



CREATE OR REPLACE VIEW expensive_products
AS
SELECT products.*
FROM products
WHERE price > (
    SELECT AVG(price)
    FROM products
);

SELECT expensive_products.*
FROM expensive_products;

DROP VIEW expensive_products;



CREATE OR REPLACE VIEW orders_statuses
AS
SELECT orders.*, order_statuses.status_name
FROM orders
         JOIN order_statuses
              ON order_statuses_order_status_id =
                 order_statuses.order_status_id;

SELECT orders_statuses.*
FROM orders_statuses;

DROP VIEW orders_statuses;



CREATE OR REPLACE VIEW products_categories
AS
SELECT products.product_title,
       categories.category_title,
       products.price
FROM products
         JOIN categories USING (category_id)
WHERE in_stock > 0
ORDER BY price DESC;

SELECT products_categories.*
FROM products_categories;

DROP VIEW products_categories;
