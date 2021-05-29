from linked_list import LinkedList


class Graph:
    """graph class"""

    def __init__(self):
        self.first = None

    class Node:
        """hash list node"""

        def __init__(self, data):
            self.connections = LinkedList()
            self.data = data

        def connect(self, node):
            """ returns next node"""
            if node:
                self.connections.append(node)

        def disconnect(self, node):
            """ det next node """
            if node:
                self.connections.remove(node)

        def get(self):
            """ returns node date """
            return self.data

        def __str__(self):
            connections = ''
            for node in self.connections:
                connections += f'[{node.data}] '
            return f'{self.data}: {connections}'

    def lookup_from_node(self, node, target, visited):
        visited.append(node)
        if target == node.data:
            return node
        for item in node.connections:
            if item in visited:
                continue
            if target == item.data:
                return item
            else:
                self.lookup_from_node(item, target, visited)
            visited.append(item)

    def lookup(self, target):
        """ return value node. """
        visited = []
        return self.lookup_from_node(self.first, target, visited)

    def insert(self, data, connections):
        """ add value node to end of list """
        if self.first:
            new_node = self.Node(data)
            for item in connections:
                node = self.lookup(item)
                if node:
                    new_node.connect(node)
                    node.connect(new_node)

        else:
            self.first = self.Node(data)

    def delete(self, data):
        target = self.lookup(data)
        print(target)
        if target:
            for item in target.connections:
                item.disconnect(target)
                target.disconnect(item)
            del target

    def __getitem__(self, key):
        return self.lookup(key)


if __name__ == "__main__":
    da_graph = Graph()
    da_graph.insert(12, None)
    da_graph.insert(22, [12])
    da_graph.insert(1, [12])
    da_graph.insert(16, [22, 12])
    da_graph.insert(16, [16, 12])
    print(da_graph.first)

    print(da_graph.lookup(16))
    da_graph.delete(16)
    print(da_graph.lookup(16))
    print(da_graph.first)
    print(da_graph.lookup(22))
    da_graph.delete(16)
    print(da_graph.lookup(16))
    print(da_graph.first)
    print(da_graph[12])
