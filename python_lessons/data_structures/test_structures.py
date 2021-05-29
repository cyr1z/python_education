"""HashTable tests"""

import pytest
from hash_table import HashTable


def test_hash_table():
    """test insert, lookup and delete"""
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


