
-- 2. Написать 2 любые хранимые процедуры с использованием
--    условий, циклов и транзакций.

CREATE MATERIALIZED VIEW city_orders_total
AS
SELECT COUNT(orders.carts_cart_id)   AS orders_count,
       SUM(orders.shipping_total)    AS total,
       (SUM(orders.shipping_total) /
        COUNT(orders.carts_cart_id)) as average_bill,
       users.city
FROM orders
         JOIN carts ON orders.carts_cart_id = carts.cart_id
         JOIN users ON users.user_id = carts.users_user_id
GROUP BY users.city
ORDER BY total;


SELECT city_orders_total.*
FROM city_orders_total;

DROP MATERIALIZED VIEW city_orders_total;


CREATE OR REPLACE
    PROCEDURE update_city_orders_total()
    LANGUAGE plpgsql
AS
$$
BEGIN
    IF EXISTS(SELECT orders.*
              FROM orders
              WHERE DATE(orders.updated_at) >= CURRENT_DATE
                AND DATE(orders.updated_at) < CURRENT_DATE + INTERVAL '1 DAY')
    THEN
        REFRESH MATERIALIZED VIEW city_orders_total;
    END IF;
END;
$$;

CALL update_city_orders_total();




CREATE OR REPLACE
    PROCEDURE rotate_logs()
    LANGUAGE plpgsql
AS
$$
DECLARE
actual_count int;
BEGIN
    DELETE
    FROM price_change_log
    where datetime < CURRENT_DATE - INTERVAL '90 DAY';
    IF 1000 > (SELECT COUNT(*) FROM price_change_log)
        THEN ROLLBACK;
    ELSE
        COMMIT;
    END IF;
END;
$$;

CALL rotate_logs();