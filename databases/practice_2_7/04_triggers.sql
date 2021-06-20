
-- 4. Добавить 2 любых триггера и обработчика к ним.

CREATE OR REPLACE
    FUNCTION check_total_bigger_then_zero()
    RETURNS TRIGGER
    LANGUAGE plpgsql
AS
$$
BEGIN
    IF NEW.total <= 0 THEN
        RAISE 'The total amount must be greater than 0';
    END IF;
    RETURN NEW;
END;
$$;

CREATE TRIGGER check_total
    BEFORE INSERT OR UPDATE
    ON orders
    FOR EACH ROW
EXECUTE FUNCTION check_total_bigger_then_zero();

UPDATE orders
SET orders.total = 100
WHERE orders.order_id = 17;

DROP TRIGGER IF EXISTS check_total ON orders;



CREATE TABLE price_change_log
(
    id         SERIAL    NOT NULL PRIMARY KEY,
    product_id INT       NOT NULL,
    old_price  FLOAT     NOT NULL,
    price      FLOAT     NOT NULL,
    datetime   TIMESTAMP NOT NULL,
    percent    FLOAT
               GENERATED ALWAYS
                   AS (round((price - old_price) / old_price * 100.0))
                   STORED
);

CREATE OR REPLACE
    FUNCTION price_change_logger()
    RETURNS TRIGGER
    LANGUAGE plpgsql
AS
$$
BEGIN
    IF NEW.price <> OLD.price THEN
        INSERT INTO price_change_log(product_id, old_price, price, datetime)
        VALUES (OLD.product_id, OLD.price, NEW.price, now());
    END IF;
    RETURN NEW;
END;
$$;

CREATE TRIGGER price_change_trigger
    AFTER UPDATE
    ON products
    FOR EACH ROW
EXECUTE PROCEDURE price_change_logger();


UPDATE products
SET price = products.price + products.price * 0.2
WHERE products.product_id = 17;

SELECT price_change_log.*
FROM price_change_log;

DROP TRIGGER IF EXISTS product_price_changes ON products;
