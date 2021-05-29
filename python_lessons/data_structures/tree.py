"""binary tree"""


class BinaryTree:
    """binary tree class"""

    class Node:
        """ class for tree nodes """

        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
            self.parent = None

        def get(self):
            """ returns node date """
            return self.data

        def get_left(self):
            """ returns next node"""
            return self.left

        def set_left(self, node):
            """ set left node """
            self.left = node

        def set_parent(self, node):
            """ set parent node """
            self.parent = node

        def get_right(self):
            """ returns right node"""
            return self.right

        def set_right(self, node):
            """ get previous node """
            self.right = node

        def set_data(self, data):
            """ setting data value """
            self.data = data

        def insert(self, data):
            """insert a node"""
            if self.data:
                if data < self.data:
                    if self.left is None:
                        new_node = self.__class__(data)
                        new_node.set_parent(self)
                        self.left = new_node
                    else:
                        self.left.insert(data)
                elif data > self.data:
                    if self.right is None:
                        new_node = self.__class__(data)
                        new_node.set_parent(self)
                        self.right = new_node
                    else:
                        self.right.insert(data)
            else:
                self.data = data

        def parent_connect(self, node):
            """connect node with parent"""
            if self.parent.get() >= self.data:
                self.parent.set_left(node)
                if node and node.left is not None:
                    node.set_parent(self.parent)
            else:
                self.parent.set_right(node)
                if node and node.left is not None:
                    node.set_parent(self.parent)

        def minimal_child_node(self):
            """ search minimal node """
            item = self
            while item.right is not None:
                item = item.right
            return item

        def delete(self):
            """ delete a node"""

            if self.left is None and self.right is None:
                self.parent_connect(None)

            elif self.left is not None and self.right is None:
                self.parent_connect(self.left)

            elif self.left is None and self.right is not None:
                self.parent_connect(self.right)

            elif self.left is not None and self.right is not None:
                mini_me = self.left.minimal_child_node()
                number = mini_me.get()
                self.set_data(number)
                mini_me.delete()

        def lookup(self, target):
            """ find a node """
            if target == self.data:
                return self
            if target < self.data and self.left is not None:
                return self.left.lookup(target)
            elif target > self.data and self.right is not None:
                return self.right.lookup(target)

        def get_tree_view(self, level=0, unit=''):
            """ make tree string """
            result = ''
            if self.left:
                result += self.left.get_tree_view(level + 1, '/')
            result += '\t' * level + f'{unit} {self.data}\n'
            if self.right:
                result += self.right.get_tree_view(level + 1, '\\')
            return result

        def __str__(self):
            result = '[' + str(self.data) + '] Left -> '
            if self.left:
                result += str(self.left.get())
            else:
                result += 'None'

            if self.right:
                result += ' Right -> ' + str(self.right.get())
            else:
                result += ' Right -> None'
            return result

    def __init__(self, data=None):
        self.root = None
        if data is not None:
            self.root = self.Node(data)

    def insert(self, data):
        """ insert new node """
        new_node = self.Node(data)
        if self.root is None:
            self.root = new_node
        else:
            self.root.insert(data)

    def lookup(self, target):
        """ find node """
        if self.root is None:
            return None
        return self.root.lookup(target)

    def delete(self, data):
        """ delete node """
        target = self.lookup(data)
        target.delete()

    def __str__(self):
        return self.root.get_tree_view()


if __name__ == "__main__":
    from random import randint

    tree = BinaryTree(randint(10, 100))
    for _ in range(10):
        tree.insert(randint(10, 100))
    print(tree)
    print(tree.lookup(42))

tree_two = BinaryTree()

nums = [45, 32, 64, 80, 21, 17, 55, 97, 33, 42, 29]
for i in nums:
    tree_two.insert(i)

print(tree_two)
tree_two.delete(45)
print(tree_two)
