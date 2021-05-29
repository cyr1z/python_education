"""Stack and Queue classes."""
from linked_list import LinkedList, DoublyLinkedLists


class Stack(LinkedList):
    """ Stck class """

    def push(self, value):
        """put node to Stack"""
        self.prepend(value)

    def pop(self):
        """get node from Stack"""
        return self.remove_first()

    def peek(self):
        """show fist node in Stack"""
        return self.first.data


class Queue(DoublyLinkedLists):
    """Queue class"""

    def enqueue(self, value):
        """put node to queue"""
        self.prepend(value)

    def dequeue(self):
        """get node from queue"""
        return self.remove_last()

    def peek(self):
        """show fist node in queue"""
        return self.last


if __name__ == "__main__":
    stack = Stack()
    print(stack)
    print(stack.pop())
    stack.push(10)
    stack.push(30)
    stack.push(5)
    print(stack)
    print(stack.pop(), stack.pop())
    print(stack.peek(), stack)

    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    print(queue)
    print(queue.peek())
    print(queue.dequeue())
    print(queue)
    print(queue.dequeue())
    print(queue)
