""" tests """

import pytest
from hash_table import HashTable
from linked_list import LinkedList, DoublyLinkedLists


def test_hash_table():
    """HashTable test insert, lookup and delete"""
    table = HashTable()
    table['AA'] = 465
    table.insert('BB', 777)
    table.insert('CC', 12)
    table.insert('DD', 99)
    table.insert('EE', 9999)
    table.insert('FF', 0)

    assert 99 in table.lookup("DD")
    assert 9999 in table["EE"]
    table.delete('DD')
    with pytest.raises(KeyError):
        table.delete('DD')


def test_linked_list():
    """ Test linked list """
    d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 113]
    my_linked_list = LinkedList(*d)
    print(my_linked_list)
    for k, i in enumerate(my_linked_list):
        assert i == d[k]
    assert len(my_linked_list) == 10
    my_linked_list.prepend(2)
    my_linked_list.insert(3)
    my_linked_list.insert(33, 5)
    assert my_linked_list[0] == 3
    assert my_linked_list[1] == 2
    assert my_linked_list[12] == 113


def test_double_linked_list():
    """Test double linked list"""
    d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 113]
    my_double_linked_list = DoublyLinkedLists(*d)
    print(my_double_linked_list)

    b = my_double_linked_list.remove_first()
    f = my_double_linked_list.remove_last()
    assert d[0] == b
    assert d[-1] == f
    my_double_linked_list.prepend(f)
    my_double_linked_list.append(b)
    assert d[0] == my_double_linked_list[-1]
    assert d[-1] == my_double_linked_list[0]
    my_double_linked_list.insert(10101, 5)
    assert my_double_linked_list[5] == 10101
    my_double_linked_list.delete(5)
    my_double_linked_list.remove(5)
    assert 5 not in my_double_linked_list
    assert 10101 not in my_double_linked_list
    my_double_linked_list.reverse()
    assert d[-1] == my_double_linked_list[-1]
    assert d[0] == my_double_linked_list[0]
    assert min(d) == my_double_linked_list[0]
    my_double_linked_list.sort()
    assert max(d) == my_double_linked_list[-1]
    my_double_linked_list[0] = 1661
    assert my_double_linked_list[0] == 1661
