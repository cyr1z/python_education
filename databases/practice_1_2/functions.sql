-- создать 2 функции (
-- одна из них должна возвращать таблицу,
-- одна из них должна использовать циклы,
-- одна из них должна использовать курсор).

create or replace
    function get_branch_clients(branch_ varchar)
    returns text
    language plpgsql
as
$$
declare
    clients     text default '';
    temp_record record;
    cursor_client cursor (branch_ varchar) for
        select branch.branch_id,
               branch.name                as branch_name,
               count(renting.renting_id),
               concat(customer.first_name, ' ',
                      customer.last_name) as customer_name
        from renting
                 join branch using (branch_id)
                 join customer using (customer_id)

        where branch.name = branch_
        group by branch.branch_id, customer.customer_id;
begin
    open cursor_client(branch_);
    loop
        fetch cursor_client into temp_record;
        exit when not found;
        clients := concat( temp_record.customer_name, '; ', clients);
    end loop;
    close cursor_client;
    return clients;
end;
$$;



select get_branch_clients('53 city_2 branch');

drop function get_branch_clients(varchar);


create or replace
    function renting_details(renting_id_ int)
    returns table
            (
                renting_id     int,
                period         interval,
                total          numeric,
                renting_date   date,
                customer_name  varchar,
                customer_phone varchar,
                branch_name    varchar,
                car_name       varchar,
                car_number     varchar
            )
    language plpgsql
as
$$
declare
    temp_record record;
begin
    for temp_record in (
        select renting.renting_id,
               renting.period,
               EXTRACT(epoch from (renting.period)) / 86400 *
               car.price                  as total,
               renting.renting_date,
               concat(customer.first_name, ' ',
                      customer.last_name) as customer_name,
               address.phone              as customer_phone,
               branch.name                as branch_name,
               car.name                   as car_name,
               car.number                 as car_number
        from renting
                 join car using (car_id)
                 join branch using (branch_id)
                 join customer using (customer_id)
                 join address on customer.address_id = address.address_id

        where renting.renting_id = renting_id_
    )
        loop
            renting_id := temp_record.renting_id;
            period := temp_record.period;
            total := temp_record.total;
            renting_date := temp_record.renting_date;
            customer_name := temp_record.customer_name;
            customer_phone := temp_record.customer_phone;
            branch_name := temp_record.branch_name;
            car_name := temp_record.car_name;
            car_number := temp_record.car_number;
            return next;
        end loop;
end;
$$;

drop function renting_details(integer);

select renting_details.*
from renting_details(7606);
