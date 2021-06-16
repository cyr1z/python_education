
COPY categories
FROM '/docker-entrypoint-initdb.d/csv/categories.csv'
DELIMITER ','
CSV;

COPY products
FROM '/docker-entrypoint-initdb.d/csv/products.csv'
DELIMITER ','
CSV;

COPY users
FROM '/docker-entrypoint-initdb.d/csv/users.csv'
DELIMITER ','
CSV;

COPY carts
FROM '/docker-entrypoint-initdb.d/csv/carts.csv'
DELIMITER ','
CSV;

COPY cart_products
FROM '/docker-entrypoint-initdb.d/csv/cart_products.csv'
DELIMITER ','
CSV;

COPY order_statuses
FROM '/docker-entrypoint-initdb.d/csv/order_statuses.csv'
DELIMITER ','
CSV;

COPY orders
FROM '/docker-entrypoint-initdb.d/csv/orders.csv'
DELIMITER ','
CSV;
