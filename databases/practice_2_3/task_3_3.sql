-- Вывести наименование группы товаров, общее количество по группе товаров в порядке убывания количества

SELECT category_title, count(*)
FROM categories
         JOIN products USING (category_id)
GROUP BY category_title
ORDER BY count(*) DESC;
