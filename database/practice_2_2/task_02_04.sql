-- Вывести:
-- 1. среднюю сумму всех завершенных сделок

SELECT AVG(orders.total)
FROM public.orders
WHERE orders.order_statuses_order_status_id = 4;

-- 2. вывести максимальную сумму сделки за 3 квартал 2020

SELECT MAX(orders.total)
FROM public.orders
WHERE orders.order_statuses_order_status_id = 4
  AND orders.created_at BETWEEN '2020-07-01' AND '2020-10-01';
