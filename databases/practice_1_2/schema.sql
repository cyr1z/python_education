create table city
(
	city_id serial not null
		constraint city_pk
			primary key,
	name varchar(50) not null
);

create unique index city_name_uindex
	on city (name);

create table street
(
	street_id serial not null
		constraint street_pk
			primary key,
	name varchar(50) not null,
	city_id int not null
		constraint street_city_city_id_fk
			references city
);

create table house
(
	house_id serial not null
		constraint house_pk
			primary key,
	name varchar(50),
	street_id int
		constraint house_street_street_id_fk
			references street
);

create table address
(
	address_id serial not null
		constraint address_pk
			primary key,
	phone varchar(25),
	city_id int
		constraint address_city_city_id_fk
			references city,
	house_id int
		constraint address_house_house_id_fk
			references house,
	street_id int
		constraint address_street_street_id_fk
			references street
);

create table car
(
	car_id serial not null
		constraint car_pk
			primary key,
	name varchar(50),
	number varchar(25) not null,
	price money
);

create unique index car_number_uindex
	on car (number);

create table customer
(
	customer_id serial not null
		constraint customer_pk
			primary key,
	first_name varchar(50),
	last_name varchar(50),
	address_id int
		constraint customer_address_address_id_fk
			references address
);

create table branch
(
	branch_id serial not null
		constraint branch_pk
			primary key,
	name varchar(50),
	address_id int
		constraint branch_address_address_id_fk
			references address
);

create table renting
(
	renting_id serial not null
		constraint renting_pk
			primary key,
	customer_id int
		constraint renting_customer_customer_id_fk
			references customer,
	car_id int not null
		constraint renting_car_car_id_fk
			references car,
	branch_id int
		constraint renting_branch_branch_id_fk
			references branch,
	renting_date date not null,
	period interval
);

