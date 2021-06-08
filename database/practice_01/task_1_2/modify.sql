alter table users add phone_number int;

alter table users alter column phone_number type varchar;

-- alter table users alter column phone_number type varchar using phone_number::varchar;