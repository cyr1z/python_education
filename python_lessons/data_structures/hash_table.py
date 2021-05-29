""" hash table """

from linked_list import LinkedList


def hash_func(value):
    """Method for calculating the hash code"""
    return sum(ord(item) for item in str(value)) % 30


class HashTable(LinkedList):
    """This is the hash table class"""

    class Node:
        """hash list node"""

        def __init__(self, key, value):
            self.hash_code = hash_func(key)
            self.next = None
            self.data = LinkedList()
            self.data.append(value)

        def set_data(self, key, value):
            """set node data"""
            if not self.hash_code:
                self.hash_code = hash_func(key)
                self.data.append(value)
            elif hash_func(key) == self.hash_code:
                self.data.append(value)
            else:
                raise ValueError("Value not for this hash_code item")

        def get(self):
            """ get node data """
            return self.data

        def get_next(self):
            """ returns next node"""
            return self.next

        def set_next(self, node):
            """ det next node """
            self.next = node

        def __str__(self):
            return str(self.hash_code) + ': ' + str(self.data)

    def append(self, key, value):
        """ add value node to end of list """
        if self.first:
            self.last.set_next(self.Node(key, value))
        else:
            self._head.set_next(self.Node(key, value))

    def prepend(self, key, value):
        """ insert value node in first position """
        temp = self.first
        self._head.set_next(self.Node(key, value))
        self.first.set_next(temp)

    def delete(self, key):
        """ delete item in key position """
        hash_code = hash_func(key)
        if self.first is None:
            raise KeyError(f"key [{key}] out of index range")
        else:
            item = self.first
            prev = self._head
            while item:
                if item.hash_code == hash_code:
                    prev.set_next(item.get_next())
                    return item.get()
                prev = item
                item = item.get_next()
        raise KeyError(f"key [{key}] out of index range")

    def lookup(self, key):
        """ return value index. """
        hash_code = hash_func(key)
        if self.first is None:
            raise KeyError(f"key [{key}] out of range")
        item = self.first
        while item.hash_code != hash_code:
            if item is None:
                raise KeyError(f"key [{key}] out of range")
            item = item.get_next()
        return item.get()

    def insert(self, key, value):
        """ insert value to key position."""
        hash_code = hash_func(key)
        prev = None
        item = self.first
        while item.hash_code != hash_code:
            if item is None:
                self.append(key, value)
                break
            prev = item
            item = item.get_next()

        new_item = self.Node(key, value)
        new_item.set_next(item.get_next())
        prev.set_next(new_item)

    def __getitem__(self, key):
        return self.lookup(key)

    def __setitem__(self, key, value):
        hash_code = hash_func(key)
        item = self.first
        while item is not None:
            if item.hash_code == hash_code:
                item.set_data(key, value)
                break
            item = item.get_next()
        else:
            self.append(key, value)


if __name__ == "__main__":
    hash_table = HashTable()
    hash_table["One"] = 5

    print(hash_table["One"])
    print(hash_table)
    hash_table["Two"] = 2
    print(hash_table)
    hash_table.insert('Two', 7)
    print(hash_table)
    hash_table.delete('One')
    print(hash_table)
