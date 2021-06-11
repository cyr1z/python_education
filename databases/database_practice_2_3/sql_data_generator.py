"""
generate sql for potential_customers

"""
from random import randint

from faker import Faker

COUNT = 100


def get_fake(f, i, city):
    return f"INSERT INTO potential_customers" \
           f" (id, email, name, surname, second_name, city) " \
           f"VALUES ({i}, '{f.email()}', '{f.first_name()}'," \
           f" '{f.last_name()}', 'second name {i}', 'city {city}');\n"


if __name__ == "__main__":
    faker = Faker()
    with open("potential_customers.sql", "w") as sql_file:
        for item in range(1, COUNT):
            city_number = randint(1, 20)
            sql_file.write(get_fake(faker, item, city_number))
