from unittest import mock

import pytest
from datetime import datetime

from software_testing.to_test import sum_all, even_odd, time_of_day, \
    Product, Shop


# even_odd
@pytest.mark.parametrize('test_arg, expected',
                         [
                             (1, 'odd'),
                             (10, 'even'),
                             (-4, 'even')
                         ])
def test_even_odd(test_arg, expected):
    assert even_odd(test_arg) == expected


def test_even_odd_none_arg_test():
    test_arg = None
    with pytest.raises(TypeError):
        even_odd(test_arg)


# sum_all
@pytest.mark.parametrize('test_arg, expected',
                         [
                             ([2, 4], 6),
                             ([-3, 9, 6], 12),
                             ([-4], -4),
                         ])
def test_sum_all(test_arg, expected):
    assert sum_all(*test_arg) == expected


def test_str_arg_test_sum_all():
    test_arg = ['None', 'tt']
    with pytest.raises(TypeError):
        sum_all(*test_arg)


def test_none_arg_test_sum_all():
    test_arg = None
    with pytest.raises(TypeError):
        sum_all(test_arg)


# time_of_day
@pytest.mark.parametrize('test_arg, expected',
                         [
                             ([2021, 1, 1, 10, 10, 10], 'morning'),
                             ([2021, 1, 1, 5, 10, 10], 'night'),
                             ([2021, 1, 1, 16, 10, 10], 'afternoon'),
                             ([2021, 1, 1, 21, 10, 10], 'night'),
                         ])
@mock.patch('software_testing.to_test.datetime')
def test_time_of_day(mocked_datetime, test_arg, expected):
    mocked_datetime.now.return_value = datetime(*test_arg)
    assert time_of_day() == expected


# Product fixtures
@pytest.fixture
def zero_quantity_product():
    """Returns a Product instance with a zero quantity."""
    return Product('zero_quantity_product', 2, 0)


@pytest.fixture
def zero_price_product():
    """Returns a Product instance with a zero price."""
    return Product('zero_price_product', 0, 1)


@pytest.fixture
def regular_product():
    """Returns a Product instance."""
    return Product('regular_product', 10, 15)


# Product tests
# subtract_quantity
def test_product_subtract_quantity(zero_price_product):
    zero_price_product.subtract_quantity()
    assert zero_price_product.quantity == 0


def test_zero_quantity_product_subtract_quantity(zero_quantity_product):
    zero_quantity_product.subtract_quantity()
    assert zero_quantity_product.quantity == -1


def test_much_product_subtract_quantity(regular_product):
    regular_product.subtract_quantity(5)
    assert regular_product.quantity == 10


# add_quantity
def test_product_add_quantity(regular_product):
    assert regular_product.quantity == 15
    regular_product.add_quantity(5)
    assert regular_product.quantity == 20


# change_price
def test_product_change_price(zero_price_product):
    assert zero_price_product.price == 0
    zero_price_product.change_price(5)
    assert zero_price_product.price == 5


# Shop fixtures
@pytest.fixture
def empty_shop():
    """Returns a Product instance with a zero quantity."""
    return Shop()


@pytest.fixture
def shop_with_one_zero_quantity_product(zero_quantity_product):
    """Returns a Shop instance with a zero quantity product."""
    return Shop(zero_quantity_product)


@pytest.fixture
def shop_with_two_products(regular_product, zero_quantity_product):
    """Returns a Shop instance."""
    return Shop([regular_product, zero_quantity_product])


# Shop tests
# add_product
def test_shop_add_product(empty_shop, regular_product, zero_price_product):
    assert empty_shop.products == []
    empty_shop.add_product(regular_product)
    assert empty_shop.products == [regular_product]
    empty_shop.add_product(zero_price_product)
    assert empty_shop.products == [regular_product, zero_price_product]
    assert empty_shop.products[1].price == 0
    assert empty_shop.products[0].title == 'regular_product'


# _get_product_index
def test_shop_get_product_index(shop_with_two_products):
    assert shop_with_two_products._get_product_index('regular_product') == 0
    assert shop_with_two_products._get_product_index(
        'zero_quantity_product') == 1
    assert shop_with_two_products._get_product_index('some_string') is None
    with pytest.raises(TypeError):
        shop_with_two_products._get_product_index()


# sell_product
def test_shop_sell_product(shop_with_two_products):
    assert shop_with_two_products.money == 0
    assert shop_with_two_products.sell_product('regular_product') == 10
    assert shop_with_two_products.products[0].quantity == 14
    with pytest.raises(TypeError):
        shop_with_two_products.sell_product()
    shop_with_two_products.sell_product('regular_product', 14)
    assert shop_with_two_products._get_product_index('regular_product') is None
    assert shop_with_two_products.money == 150


def test_shop_sell_product_zero_quantity(shop_with_one_zero_quantity_product):
    with pytest.raises(ValueError):
        shop_with_one_zero_quantity_product.sell_product('zero_quantity_product')
