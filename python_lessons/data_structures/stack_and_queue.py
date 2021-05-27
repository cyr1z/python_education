from linked_list import LinkedList, DoublyLinkedLists


class Stack(LinkedList):
    def push(self, value):
        self.prepend(value)

    def pop(self):
        return self.remove_first()

    def peek(self):
        return self.first


class Queue(DoublyLinkedLists):
    def enqueue(self, value):
        self.prepend(value)

    def dequeue(self):
        return self.remove_last()

    def peek(self):
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
