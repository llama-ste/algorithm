# Node 정의
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data, None)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data, None)

    def getNode(self, index):
        curr = 0
        node = self.head
        while curr < index:
            curr += 1
            node = node.next
        return node

    def addNode(self, index, data):
        newNode = Node(data, None)

        if index == 0:
            newNode.next = self.head
            self.head = newNode
            return

        node = self.getNode(index-1)
        nextNode = node.next
        node.next = newNode
        newNode.next = nextNode

    def deleteNode(self, index):
        if index == 0:
            self.head = self.head.next
            return
        node = self.getNode(index-1)
        node.next = node.next.next


l1 = [1,2,3,4,5]

l2 = LinkedList()

for ele in l1:
    l2.append(ele)

l2.addNode(3, 10)