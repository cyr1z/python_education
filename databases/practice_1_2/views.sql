-- создать 3 представления (
-- 1 из них должно быть материализированным
-- и хранить данные от "тяжелого" запроса).

--
create or replace view branch_detail as
select branch_id,
       branch.name,
       address.phone,
       concat(city.name, ' ', street.name, ' ', house.name) as address
from branch
         join address using (address_id)
         join city using (city_id)
         join street using (street_id)
         join house using (house_id);

drop view branch_detail;
select branch_detail.*
from branch_detail;

--
create materialized view customer_detail as
select customer_id,
       concat(customer.first_name, ' ', customer.last_name) as name,
       address.phone,
       concat(city.name, ' ', street.name, ' ', house.name) as home_address,
       last.last_renting_date,
       total_customer.sum_total as total
from customer
         join address using (address_id)
         join city using (city_id)
         join street using (street_id)
         join house using (house_id)
         join (
    select customer_id       as c_id,
           max(renting_date) as last_renting_date

    from renting
    group by customer_id
) as last on last.c_id = customer_id
         join (select customer_id as cc_id, sum(total) as sum_total
               from (select customer.customer_id,
                            EXTRACT(epoch from sum(renting.period)) / 86400 * car.price as total
                     from customer
                              join renting using (customer_id)
                              join car using (car_id)
                     group by customer.customer_id, car.price) as total
               group by customer_id
) as total_customer on total_customer.cc_id = customer.customer_id
;

drop materialized view customer_detail;

select customer_detail.*
from customer_detail;

--
create or replace view top_cars as
select car.name,
       sum(renting.period)  as rental_period,
       EXTRACT(epoch from sum(renting.period)) / 86400 * car.price as total
from car
         join renting using (car_id)
group by car.name, car.price
order by total desc
limit 25;

drop view top_cars;

select top_cars.*
from top_cars;
