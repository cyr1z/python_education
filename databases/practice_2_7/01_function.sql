-- 1. Создать функцию, которая сетит shipping_total = 0 в таблице order,
--      если город юзера равен x. Использовать IF clause.

CREATE OR REPLACE
    FUNCTION zeroing_shipping_total(target_city VARCHAR)
    RETURNS void
    LANGUAGE plpgsql
AS
$$
BEGIN
    IF EXISTS(SELECT users.user_id
              FROM users
              WHERE city = target_city)
    THEN
        UPDATE orders
        SET shipping_total = 0
        WHERE orders.order_id
                  IN (SELECT orders.order_id
                      FROM orders
                               JOIN carts
                                    ON orders.carts_cart_id = carts.cart_id
                               JOIN users
                                    ON users.user_id = carts.users_user_id
                      WHERE users.city = target_city);
    ELSE
        RAISE EXCEPTION '% city not found', target_city;
    END IF;
END;
$$;


BEGIN;

SELECT zeroing_shipping_total('city 17');

SELECT users.city, orders.shipping_total
FROM orders
         JOIN carts ON orders.carts_cart_id = carts.cart_id
         JOIN users ON users.user_id = carts.users_user_id
WHERE users.city = 'city 17';

SELECT zeroing_shipping_total('Kharkiv');

ROLLBACK;
