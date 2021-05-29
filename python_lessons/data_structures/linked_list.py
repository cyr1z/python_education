"""
data structure classes
LinkedList
"""
from copy import deepcopy


class LinkedList:
    """ Linked List class"""

    class Anchor:
        """ class for head and tail of lists """

        def __init__(self):
            self.next = None

        def set_next(self, next_node):
            """set nxt node """
            self.next = next_node

        def get_next(self):
            """ getting next node """
            return self.next

    class Node:
        """ class for lists nodes """

        def __init__(self, data):
            self.data = data
            self.next = None

        def get(self):
            """ returns node date """
            return self.data

        def get_next(self):
            """ returns next node"""
            return self.next

        def set_next(self, node):
            """ det next node """
            self.next = node

        def set_data(self, data):
            """ setting data value """
            self.data = data

        def __str__(self):
            return str(self.data)

    def __init__(self, *args):
        self._head = self.Anchor()
        self.args = args
        if self.args:
            for item in self.args:
                self.append(item)

    @property
    def last(self):
        """ return last node in list """
        item = self._head
        while item.get_next() is not None:
            item = item.next
        return item

    @property
    def first(self):
        """return first node """
        return self._head.get_next()

    def append(self, value):
        """ add value node to end of list """
        if self.first:
            self.last.set_next(self.Node(value))
        else:
            self._head.set_next(self.Node(value))

    def prepend(self, value):
        """ insert value node in first position """
        temp = self.first
        self._head.set_next(self.Node(value))
        self.first.set_next(temp)

    def remove(self, value):
        """ remove first node with value """
        if self.first is None:
            raise ValueError(f"value [{value}] not in LinkedList")
        item = self.first
        prev = self._head
        while item:
            if item.get() == value:
                prev.set_next(item.get_next())
                return value
            prev = item
            item = item.get_next()
        raise ValueError(f"value [{value}] not in LinkedList")

    def delete(self, key):
        """ delete item in key position """
        if self.first is None:
            raise KeyError(f"key [{key}] out of index range")
        if not key:
            self.remove_first()
        else:
            item = self.first
            index = 0
            prev = self._head
            while item:
                if index == key:
                    prev.set_next(item.get_next())
                    return item.get()
                prev = item
                item = item.get_next()
                index += 1
        raise KeyError(f"key [{key}] out of index range")

    def remove_first(self):
        """ remove first item """
        if not self.first:
            return None
        item = self.first
        self._head.set_next(item.get_next())
        return item.get()

    def lookup(self, value):
        """ return value index. """
        if self.first is None:
            raise ValueError(f"value [{value}] not in LinkedList")
        index = 0
        item = self.first
        while item is not None:
            if item.get() == value:
                break
            index += 1
            item = item.get_next()
        else:
            raise ValueError(f"value [{value}] not in LinkedList")
        return index

    def insert(self, value, key=0):
        """ insert value to key position."""
        if self.first is None and key:
            raise KeyError(f"key [{key}] out of index range")
        index = 0
        prev = None
        item = self.first
        while index != key:
            if item is None:
                raise KeyError(f"key [{key}] out of index range")
            prev = item
            item = item.get_next()
            index += 1

        if index:
            new_item = self.Node(value)
            prev.set_next(new_item)
            new_item.set_next(item)
        else:
            self.prepend(value)

    def sort(self):
        """ burble sort """
        length = self.__len__()
        index = 0
        while index < length - 1:
            key = 0
            item = self.first
            while item:
                if key >= length - 1 - index:
                    break
                if item.get() > item.get_next().get():
                    temp = item.get()
                    item.set_data(item.get_next().get())
                    item.get_next().set_data(temp)
                item = item.get_next()
                key += 1
            index += 1

    def sorted(self):
        """ return sorted list """
        sorted_self = deepcopy(self)
        sorted_self.sort()
        return sorted_self

    def __getitem__(self, key):
        if self.first is None:
            raise KeyError(f"key [{key}] out of index range")
        index = 0
        item = self.first
        while index != key:
            if item is None:
                raise KeyError(f"key [{key}] out of index range")
            item = item.get_next()
            index += 1
        return item.get()

    def __setitem__(self, key, value):
        if self.first is None:
            raise KeyError(f"key [{key}] out of index range")
        index = 0
        item = self.first
        while index != key:
            if item is None:
                raise KeyError(f"key [{key}] out of index range")
            item = item.get_next()
            index += 1
        item.set_data(value)

    def __sorted__(self):
        return self.sorted()

    def __len__(self):
        item = self._head
        count = 0
        while item.get_next() is not None:
            count += 1
            item = item.get_next()
        return count

    def __iter__(self):
        item = self.first
        while item is not None:
            yield item.get()
            item = item.get_next()

    def __str__(self):
        item = self.first
        string = ''
        while item is not None:
            string += str(item) + ' '
            item = item.get_next()
        return f"[{', '.join(string.split())}]"

    def __contains__(self, value):
        item = self.first
        while item is not None:
            if item.get() == value:
                return True
            item = item.get_next()
        return False


class DoublyLinkedLists(LinkedList):
    """ Doubly Linked Lists class"""

    class Node:
        """ class for lists nodes """

        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

        def get(self):
            """ returns node date """
            return self.data

        def get_next(self):
            """ returns next node"""
            return self.next

        def set_next(self, node):
            """ get next node """
            self.next = node

        def get_prev(self):
            """ returns previous node"""
            return self.prev

        def set_prev(self, node):
            """ get previous node """
            self.prev = node

        def set_data(self, data):
            """ setting data value """
            self.data = data

        def __str__(self):
            return str(self.data)

    def __init__(self, *args):
        self._tail = self.Anchor()
        super().__init__(*args)

    @property
    def last(self):
        """return last node """
        return self._tail.get_next()

    def append(self, value):
        """ add value node to end of list """
        new_node = self.Node(value)
        if self.last:
            new_node.set_prev(self.last)
            self.last.set_next(new_node)
        else:
            self._head.set_next(new_node)
        self._tail.set_next(new_node)

    def remove_first(self):
        """ remove first item """
        if not self.first:
            return None
        item = self.first
        next_node = item.get_next()
        next_node.set_prev(None)
        self._head.set_next(next_node)
        return item.get()

    def remove_last(self):
        """remove last node """
        item = self.last
        prev_node = item.get_prev()
        prev_node.set_next(None)
        self._tail.set_next(prev_node)
        return item.get()

    def pop(self):
        """remove last node """
        return self.remove_last()

    def remove(self, value):
        """ remove first node with value """
        if self.first is None:
            raise ValueError(f"value [{value}] not in LinkedList")
        item = self.first
        while item:
            if item.get() == value:
                next_node = item.get_next()
                prev_node = item.get_prev()
                prev_node.set_next(next_node)
                next_node.set_prev(prev_node)
                return value
            item = item.get_next()
        raise ValueError(f"value [{value}] not in LinkedList")

    def delete(self, key):
        """ delete item in key position """
        if self.first is None:
            raise KeyError(f"key [{key}] out of index range")
        if not key:
            self.remove_first()
        else:
            item = self.first
            index = 0
            while item:
                if index == key:
                    if item.get_next():
                        next_node = item.get_next()
                        prev_node = item.get_prev()
                        prev_node.set_next(next_node)
                        next_node.set_prev(prev_node)
                        return item.get()
                    else:
                        self.remove_last()
                item = item.get_next()
                index += 1
            raise KeyError(f"key [{key}] out of index range")

    def prepend(self, value):
        """ insert value node in first position """
        if self.first is None:
            self.append(value)
        else:
            temp = self.first
            new_node = self.Node(value)
            self._head.set_next(new_node)
            self.first.set_next(temp)
            temp.set_prev(self.first)

    def insert(self, value, key=0):
        """ insert value to key position."""
        if self.first is None and key:
            raise KeyError(f"key [{key}] out of index range")
        index = 0
        prev = None
        item = self.first
        while index != key:
            if item is None:
                raise KeyError(f"key [{key}] out of index range")
            prev = item
            item = item.get_next()
            index += 1

        if index:
            new_item = self.Node(value)
            prev.set_next(new_item)
            item.set_prev(new_item)
            new_item.set_next(item)
            new_item.set_prev(prev)

        else:
            self.prepend(value)

    def reverse(self):
        """reverse list"""
        item = self.first
        new_first = self.last
        new_last = self.first
        self._head.set_next(new_first)
        self._tail.set_next(new_last)
        while item:
            next_item = item.get_next()
            item.next, item.prev = item.prev, item.next
            item = next_item

    def __getitem__(self, key):
        if self.first is None:
            raise KeyError(f"key [{key}] out of index range")

        if key < 0:
            index = -1
            item = self.last
            while index != key:
                if item is None:
                    raise KeyError(f"key [{key}] out of index range")
                item = item.get_next()
                index -= 1
            return item.get()

        index = 0
        item = self.first
        while index != key:
            if item is None:
                raise KeyError(f"key [{key}] out of index range")
            item = item.get_next()
            index += 1
        return item.get()


if __name__ == "__main__":
    d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 113]
    kkd = LinkedList(*d)
    print(kkd)
    for i in kkd:
        print(i, ' - ', end='')
    print(len(kkd))

    print(kkd.lookup(9))
    kkd.prepend(2)
    kkd.insert(3)
    kkd.insert(33, 5)
    print(kkd)
    ddll = DoublyLinkedLists(*d)
    print(ddll)

    d = ddll.remove_first()
    f = ddll.remove_last()
    print(d, f, ddll)
    ddll.prepend(f)
    ddll.append(d)
    print(ddll)
    ddll.insert(10101, 5)

    print(ddll)
    ddll.delete(5)
    ddll.remove(5)
    print(ddll)
    ddll.reverse()
    print(ddll)
    print(6 in ddll, 66 in ddll)
    print(ddll[0], ddll[-1])
    print("sorted", ddll.sorted())
    ddll.sort()
    print(ddll)
    ddll[0] = 1661
    print(ddll)
    print(sorted(ddll))
    ddll[5] = 8080
    print(ddll)
