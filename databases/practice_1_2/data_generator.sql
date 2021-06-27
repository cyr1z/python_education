create or replace
    procedure generate_cities(count_of_cities int)
    language plpgsql
as
$$
declare
    query        varchar := 'insert into city(city_id, name) ' ||
                            'values (default, ''city_%s'');';
    result_query varchar;
begin
    for i in 1..count_of_cities
        loop
            result_query := concat(result_query, format(query, i));
        end loop;
    execute result_query;
end
$$;

--
create or replace
    procedure generate_streets(count_of_streets int)
    language plpgsql
as
$$
declare
    cities_ids   integer[];
    cities_count integer;
    query        varchar := 'insert into street(street_id, name, city_id) ' ||
                            'values (default, ''street_%s'', %s);';
    result_query varchar;
    city_id_     integer;
    number       integer;
begin
    cities_ids := array(select city_id from city order by random());
    cities_count := array_length(cities_ids, 1);
    for i in 1..count_of_streets
        loop
            if i % cities_count != 0 then
                number := i % cities_count;
            else
                number := cities_count;
            end if;
            city_id_ := cities_ids[number];
            result_query := concat(result_query, format(query, i, city_id_));
        end loop;
    execute result_query;
end ;
$$;


--
create or replace
    procedure generate_houses(count_of_house int)
    language plpgsql
as
$$
declare
    streets_count integer;
    query         varchar := 'insert into house(house_id, name, street_id) ' ||
                             'values (default, ''house %s'', %s);';
    result_query  varchar;
    street_id_    record;
    on_street     integer;
begin
    streets_count := (select count(street_id) from street);
    on_street := count_of_house / streets_count;

    for street_id_ in
        select street_id from street order by random()
        loop
            for i in 1..on_street
                loop
                    result_query := concat(result_query,
                                           format(query, i, street_id_.street_id));
                end loop;
        end loop;
    execute result_query;
end;
$$;


--
create or replace
    procedure generate_address()
    language plpgsql
as
$$
declare
    query        varchar := 'insert into address (' ||
                            'address_id, phone, city_id, house_id, street_id) ' ||
                            'values (default, %s, %s, %s, %s);';
    result_query varchar;
    temp_row     record;
begin
    for temp_row in
        select concat('1', city_id, street_id, house_id) as phone,
               city_id,
               house_id,
               street_id
        from house
                 join street using (street_id)
                 join city using (city_id)

        loop
            result_query := concat(result_query,
                                   format(
                                           query,
                                           temp_row.phone,
                                           temp_row.city_id,
                                           temp_row.house_id,
                                           temp_row.street_id)
                );
        end loop;
--     raise notice '%', result_query;
    execute result_query;
end;
$$;


create or replace
    procedure generate_cars(count_of_cars int)
    language plpgsql
as
$$
declare
    query           varchar :=
            'insert into car(car_id, name, number, price) ' ||
            'values (default, %s, %s, %s);';
    result_query    varchar;
    car_names       varchar[];
    car_names_count integer;
    number          integer;
    car_name        varchar;
    car_number      varchar;
    price           numeric;
begin
    car_names :=
            array ['Abarth', 'Alfa Romeo', 'Aston Martin', 'Audi', 'Bentley', 'BMW', 'Bugatti', 'Cadillac', 'Chevrolet', 'Chrysler', 'Citroën', 'Dacia', 'Daewoo', 'Daihatsu', 'Dodge', 'Donkervoort', 'DS', 'Ferrari', 'Fiat', 'Fisker', 'Ford', 'Honda', 'Hummer', 'Hyundai', 'Infiniti', 'Iveco', 'Jaguar', 'Jeep', 'Kia', 'KTM', 'Lada', 'Lamborghini', 'Lancia', 'Land Rover', 'Landwind', 'Lexus', 'Lotus', 'Maserati', 'Maybach', 'Mazda', 'McLaren', 'Mercedes-Benz', 'MG', 'Mini', 'Mitsubishi', 'Morgan', 'Nissan', 'Opel', 'Peugeot', 'Porsche', 'Renault', 'Rolls-Royce', 'Rover', 'Saab', 'Seat', 'Skoda', 'Smart', 'SsangYong', 'Subaru', 'Suzuki', 'Tesla', 'Toyota', 'Volkswagen', 'Volvo'];
    car_names_count := array_length(car_names, 1);
    for i in 1..count_of_cars
        loop
            if i % car_names_count != 0 then
                number := i % car_names_count;
            else
                number := car_names_count;
            end if;
            car_name := concat('''', car_names[number], ' ', i, number, '''');
            car_number :=
                    concat(left(car_name, 2), 'A', number, i, '''');
            price := floor(random() * 200 + 90)::numeric;
            result_query :=
                    concat(result_query,
                           format(query, car_name, car_number, price));
        end loop;
--     raise notice '%', result_query;
    execute result_query;
end
$$;

--

create or replace
    procedure generate_branch()
    language plpgsql
as
$$
declare
    query        varchar :=
                'insert into ' ||
                'branch(branch_id, name, address_id) ' ||
                'values (default, %s, %s);';
    result_query varchar;
    temp_row     record;
    address_id_  integer;
begin
    for temp_row in select city_id, name from city
        loop
            address_id_ := (select address_id
                            from address
                            where city_id = temp_row.city_id
                            limit 1)::integer;
            result_query := concat(result_query,
                                   format(
                                           query,
                                           concat('''',
                                                  temp_row.city_id, ' ',
                                                  temp_row.name, ' branch',
                                                  ''''),
                                           address_id_)
                );
        end loop;
    execute result_query;
end
$$;

--
--

create or replace
    procedure generate_customers()
    language plpgsql
as
$$
declare
    query            varchar :=
                'insert into ' ||
                'customer (customer_id, first_name, last_name, address_id) ' ||
                'values (default, %s, %s, %s);';
    result_query     varchar;
    temp_row         record;
    address_id_      integer;
    first_names      varchar[];
    last_names       varchar[];
    first_name_      varchar;
    last_name_       varchar;
    first_name_count integer;
    last_name_count  integer;
    index            integer;
    number           integer;
begin
    first_names :=
            array ['Adam', 'Alex', 'Aaron', 'Ben', 'Carl', 'Dan', 'David', 'Edward', 'Fred', 'Frank', 'George', 'Hal', 'Hank', 'Ike', 'John', 'Jack', 'Joe', 'Larry', 'Monte', 'Matthew', 'Mark', 'Nathan', 'Otto', 'Paul', 'Peter', 'Roger', 'Rover', 'Steve', 'Thomas', 'Tim', 'Ty', 'Victor', 'Walter'];

    last_names :=
            array ['Anderson', 'Ashwoon', 'Aikin', 'Bateman', 'Bongard', 'Bowers', 'Boyd', 'Cannon', 'Cast', 'Deitz', 'Dewalt', 'Ebner', 'Frick', 'Hancock', 'Haworth', 'Hesch', 'Hoffman', 'Kassing', 'Knutson', 'Lawless', 'Lawicki', 'Mccord', 'McCormack', 'Miller', 'Myers', 'Nugent', 'Ortiz', 'Orwig', 'Ory', 'Paiser', 'Pak', 'Pettigrew', 'Quinn', 'Quizoz', 'Ramachandran', 'Resnick', 'Sagar', 'Schickowski', 'Schiebel', 'Sellon', 'Severson', 'Shaffer', 'Solberg', 'Soloman', 'Sonderling', 'Soukup', 'Soulis', 'Stahl', 'Sweeney', 'Tandy', 'Trebil', 'Trusela', 'Trussel', 'Turco', 'Uddin', 'Uflan', 'Ulrich', 'Upson', 'Vader', 'Vail', 'Valente', 'Van Zandt', 'Vanderpoel', 'Ventotla', 'Vogal', 'Wagle', 'Wagner', 'Wakefield', 'Weinstein', 'Weiss', 'Woo', 'Yang', 'Yates', 'Yocum', 'Zeaser', 'Zeller', 'Ziegler', 'Bauer', 'Baxster', 'Casal', 'Cataldi', 'Caswell', 'Celedon', 'Chambers', 'Chapman', 'Christensen', 'Darnell', 'Davidson', 'Davis', 'DeLorenzo', 'Dinkins', 'Doran', 'Dugelman', 'Dugan', 'Duffman', 'Eastman', 'Ferro', 'Ferry', 'Fletcher', 'Fietzer', 'Hylan', 'Hydinger', 'Illingsworth', 'Ingram', 'Irwin', 'Jagtap', 'Jenson', 'Johnson', 'Johnsen', 'Jones', 'Jurgenson', 'Kalleg', 'Kaskel', 'Keller', 'Leisinger', 'LePage', 'Lewis', 'Linde', 'Lulloff', 'Maki', 'Martin', 'McGinnis', 'Mills', 'Moody', 'Moore', 'Napier', 'Nelson', 'Norquist', 'Nuttle', 'Olson', 'Ostrander', 'Reamer', 'Reardon', 'Reyes', 'Rice', 'Ripka', 'Roberts', 'Rogers', 'Root', 'Sandstrom', 'Sawyer', 'Schlicht', 'Schmitt', 'Schwager', 'Schutz', 'Schuster', 'Tapia', 'Thompson', 'Tiernan', 'Tisler' ];
    first_name_count := array_length(first_names, 1);
    last_name_count := array_length(last_names, 1);

    index := 1;
    for temp_row in
        select address_id
        from address
        where address_id not in (select address_id from branch)
        loop
            address_id_ := temp_row.address_id;

            if index % first_name_count != 0 then
                number := index % first_name_count;
            else
                number := first_name_count;
            end if;

            first_name_ := concat('''', first_names[number], '''');

            if index % last_name_count != 0 then
                number := index % last_name_count;
            else
                number := last_name_count;
            end if;

            last_name_ := concat('''', last_names[number], '''');

            result_query := concat(result_query,
                                   format(
                                           query,
                                           first_name_,
                                           last_name_,
                                           address_id_)
                );
            index := index + 1;
        end loop;
    execute result_query;
end
$$;

--

create or replace
    procedure generate_renting(max_renting int)
    language plpgsql
as
$$
declare
    query         varchar :=
                'insert into ' ||
                'renting (renting_id, customer_id, car_id, branch_id, renting_date, period) ' ||
                'values (default, %s, %s, %s, %s, %s);';
    result_query  varchar;
    temp_row      record;
    car_id_       integer;
    renting_date_ varchar;
    period_       varchar;
    rent_count_   integer;

begin
    for temp_row in
        select customer_id, branch_id
        from customer
                 join address using (address_id)
                 join (select branch_id, city_id as b_city_id
                       from branch
                                join address using (address_id)) as branch_
                      on branch_.b_city_id = city_id
        loop
            rent_count_ := random() * max_renting + 1;

            for i in 1..rent_count_
                loop
                    car_id_ :=
                            (select car_id from car order by random() limit 1);
                    renting_date_ := (select date_char
                                      from (select TO_CHAR(day, 'YYYY-MM-DD') as date_char,
                                                   round(5000 * random())     as value
                                            FROM generate_series(
                                                         '2014-10-22'::date,
                                                         '2020-12-31'::date,
                                                         '1 day'::interval) day
                                            order by value) as dcv
                                      limit 1);
                    renting_date_ := concat('''', renting_date_,'''');
                    period_ := concat('''',round(random() * 10 + 1), ' day''');
                    result_query := concat(result_query,
                                           format(
                                                   query,
                                                   temp_row.customer_id,
                                                   car_id_,
                                                   temp_row.branch_id,
                                                   renting_date_,
                                                   period_
                                               )
                        );
                end loop;
        end loop;
--     raise notice '%', result_query;
    execute result_query;
end
$$;

--
begin;

call generate_cities(50);

call generate_streets(555);

call generate_houses(4000);

call generate_address();

call generate_cars(2000);

call generate_branch();

call generate_customers();

call generate_renting(8);

select city.*
from city;

select street.*
from street;

select house.*
from house;

select address.*
from address;

select car.*
from car;

select branch.*
from branch;

select customer.*
from customer;

select first_name, last_name, count(*)
from customer
group by first_name, last_name;

select renting.*
from renting;

rollback;

commit;


