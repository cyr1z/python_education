from quick_sort import quicksort


def test_quicksort():
    assert quicksort([1]) == [1]
    assert quicksort([1,2]) == [1,2]
    assert quicksort([1,2,3]) == [1,2,3]
    assert quicksort([1,2,3,4]) == [1,2,3,4]
    assert quicksort([2,1,3,4]) == [1,2,3,4]
    assert quicksort([1,3,2,4]) == [1,2,3,4]
    assert quicksort([1,2,4,3]) == [1,2,3,4]
    assert quicksort([2,1,1,1]) == [1,1,1,2]
    assert quicksort([1,2,1,1]) == [1,1,1,2]
    assert quicksort([1,1,2,1]) == [1,1,1,2]
    assert quicksort([1,1,1,2]) == [1,1,1,2]