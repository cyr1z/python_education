-- Вывести заказы, которые успешно доставлены и оплачены

SELECT orders.*
FROM public.orders
WHERE order_statuses_order_status_id = 4;

SELECT orders.*
FROM public.orders
         JOIN public.order_statuses ON order_statuses.order_status_id =
                                       order_statuses_order_status_id
WHERE order_statuses.status_name = 'Finished';

