-- Задание 1
-- Создайте новую таблицу potential customers с полями id, email, name, surname, second_name, city

CREATE TABLE IF NOT EXISTS potential_customers
(
    id          integer PRIMARY KEY,
    email       varchar(50),
    name        varchar(50),
    surname     varchar(50),
    second_name varchar(50),
    city        varchar(50)
);

-- Выведите имена и электронную почту потенциальных и существующих пользователей из города city 17

SELECT CONCAT(name, ' ', surname) AS name, email
FROM potential_customers
WHERE city = 'city 17'
UNION
SELECT CONCAT(first_name, ' ', last_name) AS name, email
FROM users
WHERE city = 'city 17';
