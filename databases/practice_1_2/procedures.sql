-- Написать 2 любые хранимые процедуры.
-- В них использовать транзакции для insert, update, delete.


create or replace
    procedure add_or_update_car(car_name varchar, car_number varchar,
                                car_price numeric)
    language plpgsql
as
$$
declare
    query varchar :=
            'insert into car(car_id, name, number, price) ' ||
            'values (''%s'', ''%s'', ''%s'', ''%s'');';
begin
    if length(car_number) < 4 then
        rollback;
        raise exception 'invalid car number %', car_number;
    end if;
    if car_price <= 0 then
        rollback;
        raise exception 'invalid price %', car_price;
    end if;
    if exists(select car.number
              from car
              where car.number = car_number)
    then
        update car
        set name  = car_name,
            price = car_price
        where car.number = car_number;
    else
        query = format(query, default, car_name, car_number, car_price);
        execute query;
    end if;
end
$$;

call add_or_update_car('monica', 'sq19f', 30);

drop procedure add_or_update_car;


create or replace
    procedure del_old_renting(years int)
    language plpgsql
as
$$
declare
    old_age   date;
begin
    old_age = now() - format('%s years', years)::interval;
    delete
    from renting
    where renting.renting_date < old_age;
end;
$$;

select renting.renting_date
from renting
order by renting.renting_date
limit 50;

call del_old_renting(4);

drop procedure del_old_renting;
