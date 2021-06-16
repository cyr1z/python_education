-- Использовать транзакции для insert, update, delete на 3х таблицах.
-- Предоставить разнообразные примеры включая возврат к savepoints.

BEGIN;

UPDATE potential_customers
SET second_name = surname
WHERE id < 10;

SAVEPOINT undelete_911_point;

DELETE
FROM potential_customers
where city LIKE '%11%'
  AND second_name LIKE '%9%';

ROLLBACK TO undelete_911_point;

COMMIT;



BEGIN;

SAVEPOINT password_restore_point;

UPDATE users
SET password = 'qwerty'
WHERE is_staff = 1;

ROLLBACK TO password_restore_point;



BEGIN;

SAVEPOINT undo_point;

INSERT INTO order_statuses
VALUES (6, 'Returns');

INSERT INTO cart_products
VALUES (1, 42),
       (2, 24);

SAVEPOINT undelete_point;

DELETE
FROM cart_products
WHERE carts_cart_id
          IN (
          SELECT carts_cart_id
          FROM cart_products
          WHERE carts_cart_id % 2 = 1
      );

ROLLBACK TO undo_point;

INSERT INTO categories
VALUES (21, '21', '21');

COMMIT;
