""" tests """

import pytest

from graph import Graph
from hash_table import HashTable
from linked_list import LinkedList, DoublyLinkedLists
from stack_and_queue import Stack, Queue
from tree import BinaryTree


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


def test_stack():
    stack = Stack()
    assert len(stack) == 0
    assert stack.pop() is None
    stack.push(10)
    stack.push(30)
    stack.push(5)
    assert (stack.pop(), stack.pop()) == (5, 30)
    assert stack.peek() == 10


def test_queue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    assert queue.peek() == 1
    assert queue.dequeue() == 1
    assert len(queue) == 3
    assert queue.dequeue() == 2


@pytest.fixture
def graph():
    da_graph = Graph()
    da_graph.insert(12, None)
    da_graph.insert(22, [12])
    da_graph.insert(1, [12])
    da_graph.insert(16, [22, 12])

    return da_graph


def test_graph(graph):
    assert 16 in (_.get() for _ in graph[12].connections)
    graph.delete(16)
    assert 16 not in (_.get() for _ in graph[12].connections)


@pytest.fixture
def tree():
    tree_two = BinaryTree()
    nums = [45, 32, 64, 80, 21, 17, 55, 97, 33, 42, 29]
    for i in nums:
        tree_two.insert(i)
    return tree_two


def test_tree(tree):
    d = tree.lookup(21)
    assert d.get() == 21
    assert d.get_right().get() == 29
    assert d.get_left().get() == 17
    assert tree.lookup(11111) is None
    tree.delete(45)
    assert tree.lookup(42).get_right().get() == 64
    assert tree.lookup(42).get_left().get() == 32