-- 1. Продукты, цена которых больше 80.00 и меньше или равно 150.00

SELECT products.*
FROM public.products
WHERE price BETWEEN 80 AND 150;

SELECT products.*
FROM public.products
WHERE price <= 151.00
  AND price > 80;

-- 2. заказы совершенные после 01.10.2020 (поле created_at)

SELECT orders.*
FROM public.orders
WHERE created_at >= '2020-10-01';

-- 3. заказы полученные за первое полугодие 2020 года

SELECT orders.*
FROM public.orders
WHERE created_at >= '2020-01-01'
  AND created_at < '2020-07-01';

SELECT orders.*
FROM public.orders
WHERE created_at BETWEEN '2020-01-01' AND '2020-06-30';

-- 4. продукты следующих категорий Category 7, Category 11, Category 18

SELECT products.*
FROM public.products
         JOIN public.categories
              ON categories.category_id = products.category_id
WHERE category_title IN ('Category 7', 'Category 11', 'Category 18');

-- 5. незавершенные заказы по состоянию на 31.12.2020

SELECT orders.*
FROM public.orders
WHERE created_at <= '2020-12-31'
  AND order_statuses_order_status_id < 4;

-- 6.Вывести все корзины, которые были созданы, но заказ так и не был оформлен.

SELECT carts.*
FROM public.carts
WHERE cart_id NOT IN (SELECT carts_cart_id FROM public.orders);

SELECT carts.*
FROM public.carts
WHERE NOT EXISTS(
        SELECT carts_cart_id
        FROM public.orders
        WHERE carts_cart_id = carts.cart_id);
