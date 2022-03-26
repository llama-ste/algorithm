class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next


# Linked List로 구현한 스택이다.
class Stack:
    def __init__(self):
        self.top = None

    def push(self, item):
        self.top = Node(item, self.top)

    def pop(self):
        if self.is_empty():
            print("Stack is empty!")
            return None

        top = self.top
        self.top = self.top.next
        return top.item

    def peek(self):
        if self.is_empty():
            print("Stack is empty!")
            return None
        return self.top.item

    def is_empty(self):
        return self.top is None


# python list기능으로 구현한 스택이다.
class Stack2:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            print("Stack is empty!")
            return None
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            print("Stack is empty!")
            return None
        return self.stack[-1]

    def is_empty(self):
        return not self.stack
