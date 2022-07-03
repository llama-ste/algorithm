class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append((data))

    def pop(self):
        popObj = None
        if len(self.stack) == 0:
            popObj = -1
        else:
            popObj = self.stack.pop()
        return popObj

    def size(self):
        return len(self.stack)

    def top(self):
        topObj = None
        if len(self.stack) == 0:
            topObj = -1
        else:
            topObj = self.stack[-1]
        return topObj

    def empty(self):
        emp = 0
        if len(self.stack) == 0:
            emp = 1
        return emp