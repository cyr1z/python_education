create table categories
(
    category_id serial not null constraint categories_pk primary key,
    category_title       varchar(255),
    category_description text
);

create table products
(
    product_id serial not null constraint products_pk primary key,
    product_title varchar(255) not null,
    product_descriptions text,
    in_stock integer,
    price double precision not null,
    slug varchar(45),
    category_id integer constraint products_categories__fk references categories on update cascade on delete cascade
);

create table users
(
    user_id serial not null constraint users_pk primary key,
    email varchar(255) not null,
    password varchar(255) not null,
    first_name varchar(255),
    last_name varchar(255),
    middle_name varchar(255),
    is_staff smallint,
    country varchar(255),
    city varchar(255),
    address text
);

create unique index users_email_uindex on users (email);

create table carts
(
	cart_id serial not null constraint carts_pk primary key,
	users_user_id int constraint carts_users_user_id_fk references users,
	subtotal decimal,
	total decimal,
	timestamp timestamp
);

create table cart_products
(
	carts_cart_id int constraint cart_products_carts_cart_id_fk references carts on update cascade on delete cascade,
	products_product_id int constraint cart_products_products_product_id_fk references products on update cascade on delete cascade
);

create table order_statuses
(
	order_status_id serial not null constraint order_statuses_pk primary key,
	status_name varchar(256)
);

create table orders
(
	order_id serial not null constraint order_pk primary key,
	carts_cart_id int constraint orders_carts_cart_id_fk references carts,
	order_statuses_order_status_id int constraint orders_order_statuses_order_status_id_fk references order_statuses,
	shipping_total decimal,
	total decimal,
	created_at timestamp,
	updated_at timestamp
);
