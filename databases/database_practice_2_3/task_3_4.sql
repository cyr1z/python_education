-- 1. Вывести продукты, которые ни разу не попадали в корзину.

SELECT products.*
FROM products
    EXCEPT (
         SELECT products.*
         FROM products
                  JOIN cart_products
                       ON products.product_id =
                          cart_products.products_product_id
     );


-- 2. Вывести все продукты, которые так и не попали ни в 1 заказ. (но в корзину попасть могли).

SELECT products.*
FROM products
    EXCEPT (
         SELECT p.*
         FROM products p
                  JOIN cart_products
                       ON p.product_id = cart_products.products_product_id
                  JOIN carts
                       ON carts.cart_id = cart_products.carts_cart_id
                  JOIN orders
                       ON orders.carts_cart_id = carts.cart_id
     );

-- 3. Вывести топ 10 продуктов, которые добавляли в корзины чаще всего.

SELECT count(*), products.product_title
FROM products
         JOIN cart_products
              ON products.product_id = cart_products.products_product_id
GROUP BY products.product_title
ORDER BY count(*) DESC
LIMIT 10;

-- 4. Вывести топ 10 продуктов, которые не только добавляли в корзины, но и оформляли заказы чаще всего.

SELECT count(orders.order_id) AS orders_count, products.product_title
FROM products
         JOIN cart_products
              ON products.product_id = cart_products.products_product_id
         JOIN carts
              ON carts.cart_id = cart_products.carts_cart_id
         JOIN orders
              ON orders.carts_cart_id = carts.cart_id
GROUP BY products.product_title
ORDER BY orders_count DESC
LIMIT 10;

-- 5. Вывести топ 5 юзеров, которые потратили больше всего денег (total в заказе).

SELECT CONCAT(first_name, ' ', last_name) AS top_user,
       sum(orders.total)                  AS total
FROM users
         JOIN carts
              ON users.user_id = carts.users_user_id
         JOIN orders
              ON orders.carts_cart_id = carts.cart_id
         JOIN order_statuses
              ON order_statuses.order_status_id =
                 orders.order_statuses_order_status_id
WHERE order_statuses.order_status_id = 4
GROUP BY user_id
ORDER BY total DESC
LIMIT 5;

-- 6. Вывести топ 5 юзеров, которые сделали больше всего заказов (кол-во заказов).

SELECT CONCAT(first_name, ' ', last_name),
       count(orders.order_id) AS purchase_count
FROM users
         JOIN carts
              ON users.user_id = carts.users_user_id
         JOIN orders
              ON orders.carts_cart_id = carts.cart_id
GROUP BY user_id;

-- 7. Вывести топ 5 юзеров, которые создали корзины, но так и не сделали заказы.

SELECT CONCAT(first_name, ' ', last_name) as top_canceled_user,
       sum(orders.total)                  AS total
FROM users
         JOIN carts
              ON users.user_id = carts.users_user_id
         JOIN orders
              ON orders.carts_cart_id = carts.cart_id
         JOIN order_statuses
              ON order_statuses.order_status_id =
                 orders.order_statuses_order_status_id
WHERE order_statuses.order_status_id = 5
GROUP BY user_id
ORDER BY total DESC
limit 5;
