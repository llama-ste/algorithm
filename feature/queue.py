class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next


# Linked List로 구현한 큐다.
class Queue:
    def __init__(self):
        self.front = None

    def enqueue(self, item):
        if not self.front:
            self.front = Node(item)
            return

        node = self.front
        while node.next:
            node = node.next
        node.next = Node(item)

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!")
            return None

        node = self.front
        self.front = node.next
        return node.item

    def peek(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        return self.front.item

    def is_empty(self):
        return self.front is None


# Python list 기능으로 구현한 큐다.
class Queue2:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!")
            return None

        front = self.queue[0]
        self.queue = self.queue[1:]
        return front

    def peek(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        return self.queue[0]

    def is_empty(self):
        return not self.queue