""" test binary search """
from binary_search import binary_search


def test_search():
    testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42, ]
    assert binary_search(testlist, 3) is None
    assert binary_search(testlist, 13) == 4
