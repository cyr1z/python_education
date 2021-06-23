-- придумать 3 различных запроса select с осмысленным использованием разных
-- видов join.
-- используя explain добавить только необходимые индексы для
-- уменьшения стоимости (cost) запросов.

--

explain(analyse)
select renting.renting_id,
       car.name                           car_name,
       concat(customer.first_name,
              ' ', customer.last_name) as customer_name,
       city.name                          customer_city
from renting
         join car using (car_id)
         join customer using (customer_id)
         join address using (address_id)
         join city using (city_id);

create index idx_city on city (name);
create index idx_customer_id on renting (customer_id);
create index idx_customer_name on customer (first_name, last_name);
create index idx_car_name on car (name);

drop index idx_city;
drop index idx_customer_id;
drop index idx_customer_name;
drop index idx_car_name;



explain(analyse)
select count(renting.renting_id) as renting_count, car.car_id
from renting
         join car using (car_id)
group by car.car_id
order by renting_count desc;

create index idx_car_number on renting (car_id, renting_id);
drop index idx_car_number;



explain
select customer.customer_id, car.name, car.number, address.phone
from customer
         join renting using(customer_id)
         left join car using (car_id)
         join address using (address_id)
where address.phone like '16%';


create index idx_phone on address (phone);
drop index idx_phone;