class MyCircularQueue:
    def __init__(self, k: int):
        # 저장 공간을 미리 정해두고 tail과 head를 이동시키는게 핵심이다.
        self.capacity = k
        self.queue = [None] * self.capacity
        self.tail = -1
        self.head = 0
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.size == self.capacity:
            print("Error: Queue is Full")
            return False
        else:
            # 저장공간을 넘어서면 안되기 때문에 저장공간으로 나눠서 나머지를 기준으로 더해준다.
            self.tail = (self.tail + 1) % self.capacity
            self.queue[self.tail] = value
            self.size += 1
            return True

    def deQueue(self) -> bool:
        if self.size == 0:
            print("Error: Queue is Empty")
            return False
        else:
            # deq = self.queue[self.head]
            self.queue[self.head] = None
            self.head = (self.head + 1) % self.capacity
            self.size -= 1
            return True # deq

    def front(self) -> int:
        if self.queue[self.head] == None:
            return -1
        else:
            findHead = self.queue[self.head]
            return findHead

    def rear(self) -> int:
        if self.queue[self.tail] == None:
            return -1
        else:
            findTail = self.queue[self.tail]
            return findTail

    def isEmpty(self) -> bool:
        empty = False
        if self.size == 0:
            empty = True
        return empty

    def isFull(self) -> bool:
        full = False
        if self.size == self.capacity:
            full = True
        return full

ringBuffer = MyCircularQueue(5)

