-- добавить 2 триггера (
-- один из них до операции по изменению данных,
-- второй после)
-- и функции или процедуры-обработчики к ним.

create or replace
    function check_phone_number()
    returns trigger
    language plpgsql
as
$$
begin
    if length(new.phone) = 0
    then
        new.phone = null;
    end if;
    if length(new.phone) > 9
           and substring(new.phone, 1, 1)::integer = 1
        or new.phone is null
    then
        return new;
    else
        raise exception 'invalid phone number';
    end if;

end;
$$;


create
    trigger phone_number_check
    before update
    on address
    for each row
execute function check_phone_number();

drop trigger phone_number_check on address;

select address.*
from address
where address.address_id = 17;

update address
set phone = '1111111144'
where address_id = 17;

update address
set phone = ''
where address_id = 17;

update address
set phone = '2111111144'
where address_id = 17;

update address
set phone = '1'
where address_id = 17;

update address
set phone = null
where address_id = 17;

--

create or replace
    function check_renting_period()
    returns trigger
    language plpgsql
as
$$
begin
    if new.period > '10 days'::interval then
        raise 'Long period. Period must be less than 10 days';
    end if;
    return new;
end;
$$;

create trigger period_check
    after insert or update
    on renting
    for each row
execute procedure check_renting_period();

update renting
set period = '9 days'::interval
where renting.renting_id = 7707;

update renting
set period = '17 days'::interval
where renting.renting_id = 7707;

select renting.*
from renting
where renting_id = 7707;

drop trigger period_check on renting;