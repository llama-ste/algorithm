class MyQueue:
    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        pop_obj = None
        if self.empty():
            print("Stack is Empty")
        else:
            pop_obj = self.queue[0]
            self.queue = self.queue[1:]
        return pop_obj

    def peek(self) -> int:
        peek_obj = None
        if self.empty():
            print("Stack is Empty")
        else:
            peek_obj = self.queue[0]
        return peek_obj

    def empty(self) -> bool:
        is_empty = None
        if len(self.queue) == 0:
            is_empty = True
        return is_empty

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()