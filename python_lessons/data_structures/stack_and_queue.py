"""Stack and Queue classes."""
from linked_list import LinkedList, DoublyLinkedLists


class Stack(LinkedList):
    """ Stack class """

    def push(self, value):
        """put node to Stack"""
        self.prepend(value)

    def pop(self):
        """get node from Stack"""
        return self.remove_first()

    def peek(self):
        """show fist node in Stack"""
        return self.first.get()


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
        return self.last.get()
