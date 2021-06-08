SELECT first_name, last_name
FROM actor;

SELECT first_name || ' ' || last_name AS Actor_Name
FROM actor;

SELECT actor_id,
       first_name,
       last_name
FROM actor
WHERE first_name LIKE 'JOE';

SELECT *
FROM actor
WHERE last_name similar to '%[GEN]%';

SELECT *
FROM actor
WHERE last_name ilike '%GEN%';

SELECT *
FROM actor
WHERE last_name ilike '%LI%'
ORDER BY last_name, first_name;

SELECT country_id, country
FROM country
WHERE country IN ('Afghanistan', 'Bangladesh', 'China');

ALTER TABLE actor
    ADD COLUMN middle_name VARCHAR(255);

ALTER TABLE actor
    ALTER COLUMN middle_name TYPE TEXT;

SELECT column_name, data_type
FROM information_schema.columns
WHERE table_name = 'actor';

ALTER TABLE actor
    DROP COLUMN middle_name;

SELECT last_name, count(last_name)
FROM actor
GROUP BY last_name;

SELECT last_name, count(last_name)
FROM actor
GROUP BY last_name
HAVING count(last_name) > 1;

UPDATE actor
SET first_name = 'HARPO'
WHERE first_name = 'GROUCHO';

SELECT first_name, last_name
FROM actor
WHERE first_name LIKE 'HARPO';

UPDATE actor
SET first_name =
        CASE
            WHEN first_name = 'HARPO' THEN
                'GROUCHO'
            WHEN first_name = 'GROUCHO' THEN
                'MUCHO GROUCHO'
            ELSE first_name
            END
WHERE actor_id = 172;

SELECT actor_id
FROM actor
WHERE first_name = 'HARPO'
  AND last_name = 'WILLIAMS';

SELECT s.first_name,
       s.last_name,
       a.address
FROM staff s
         LEFT JOIN address a
                   USING (address_id);

SELECT p.staff_id,
       COUNT(p.amount)
FROM payment p
         LEFT JOIN staff s
                   ON p.staff_id = s.staff_id
GROUP BY p.staff_id;

SELECT f.title,
       COUNT(fa.actor_id) AS number_of_actors
FROM film f
         INNER JOIN film_actor fa
                    ON f.film_id = fa.film_id
GROUP BY f.title;

SELECT f.title,
       count(i.inventory_id) AS number_of_copies
FROM film f
         JOIN inventory i
              ON f.film_id = i.film_id
WHERE f.title = 'HUNCHBACK IMPOSSIBLE'
GROUP BY f.title;

SELECT c.last_name,
       COUNT(p.amount) AS amount
FROM customer c
         LEFT JOIN payment p
                   ON c.customer_id = p.customer_id
GROUP BY c.last_name
ORDER BY c.last_name;

SELECT title
FROM film
WHERE language_id = 1
    AND title LIKE 'K%'
   OR title LIKE 'Q%';

SELECT s.first_name
FROM (SELECT a.first_name,
             a.last_name,
             f.title
      FROM actor a
               JOIN film_actor fa
                    ON a.actor_id = fa.actor_id
               JOIN film f
                    ON f.film_id = fa.film_id
      WHERE title = 'ALONE TRIP') s
GROUP BY s.first_name, s.last_name
ORDER BY s.last_name;


SELECT c.last_name,
       c.first_name,
       c.email
FROM customer c
         JOIN address a
              ON c.address_id = a.address_id
         JOIN city ci
              ON a.city_id = ci.city_id
         JOIN country co
              ON ci.country_id = co.country_id
WHERE country = 'Canada'
ORDER BY last_name;

SELECT title
FROM film f
         JOIN film_category fc
              ON f.film_id = fc.film_id
         JOIN category c
              ON fc.category_id = c.category_id
WHERE c.category_id = 8;

SELECT COUNT(r.inventory_id) AS rental_count
FROM film f
         JOIN inventory i
              ON f.film_id = i.film_id
         JOIN rental r
              ON i.inventory_id = r.inventory_id
GROUP BY f.title
ORDER BY rental_count DESC;

SELECT str.store_id,
       SUM(p.amount) AS total_sales
FROM store str
         JOIN staff stf
              ON str.store_id = stf.store_id
         JOIN payment p
              ON stf.staff_id = p.staff_id
GROUP BY str.store_id;

SELECT ci.city,
       co.country
FROM store s
         JOIN address a
              ON s.address_id = a.address_id
         JOIN city ci
              ON a.city_id = ci.city_id
         JOIN country co
              ON ci.country_id = co.country_id;

SELECT c.name,
       SUM(p.amount) AS gross_revenue
FROM category c
         JOIN film_category fc
              ON c.category_id = fc.category_id
         JOIN inventory i
              ON fc.film_id = i.film_id
         JOIN rental r
              ON i.inventory_id = r.inventory_id
         JOIN payment p
              ON r.rental_id = p.rental_id
GROUP BY c.name
ORDER BY gross_revenue DESC
limit 5;

CREATE OR REPLACE VIEW top_five_grossing_genres AS
SELECT c.name,
       SUM(p.amount) AS gross_revenue
FROM category c
         JOIN film_category fc
              ON c.category_id = fc.category_id
         JOIN inventory i
              ON fc.film_id = i.film_id
         JOIN rental r
              ON i.inventory_id = r.inventory_id
         JOIN payment p
              ON r.rental_id = p.rental_id
GROUP BY c.name
ORDER BY gross_revenue DESC
limit 50;

SELECT *
FROM top_five_grossing_genres;

DROP VIEW top_five_grossing_genres;

SELECT table_name
FROM INFORMATION_SCHEMA.views;

SELECT schemaname, viewname
FROM pg_catalog.pg_views
WHERE schemaname NOT IN ('pg_catalog', 'information_schema')
ORDER BY schemaname, viewname;

SELECT f.title,
       count(i.inventory_id) AS number_of_copies
FROM film f
         JOIN inventory i
              ON f.film_id = i.film_id
GROUP BY f.title;