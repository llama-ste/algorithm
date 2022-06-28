class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        dequeueObj = None
        if self.isEmpty():
            print("Queue is empty!")
        else:
            dequeueObj = self.queue[0]
            self.queue = self.queue[1:]
        return dequeueObj

    def peek(self):
        peekObj = None
        if self.isEmpty():
            print("Queue is empty!")
        else:
            peekObj = self.queue[0]
        return peekObj

    def isEmpty(self):
        empty = False
        if len(self.queue) == 0:
            empty = True
        return empty


que = Queue()

que.enqueue(1)
que.enqueue(2)

print(que.queue)
print(que.peek())
print(que.isEmpty())