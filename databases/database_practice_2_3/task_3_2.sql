-- Вывести имена и электронные адреса всех users отсортированных по городам и по имени (по алфавиту)

SELECT first_name, email
FROM users
ORDER BY city, first_name;