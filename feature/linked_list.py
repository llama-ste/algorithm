class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, item):
        if self.head is None:
            self.head = Node(item, None)
            return

        node = self.head
        while node.next:
            node = node.next
        node.next = Node(item, None)

    def get_node(self, index):
        if self.head is None:
            print("List is empty!")
            return None

        curr = 0
        node = self.head
        try:
            while curr < index:
                curr += 1
                node = node.next
            return node
        except:
            print("List is shorter than the index!")
            return

    def add_node(self, index, item):
        new_node = Node(item, None)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        try:
            node = self.get_node(index - 1)
            next_node = node.next
            node.next = new_node
            next_node.next = next_node
        except:
            print("List is shorter than the index!")
            return

    def delete_node(self, index):
        if self.head is None:
            print("List is empty!")
            return

        try:
            node = self.get_node(index-1)
            node.next = node.next.next
        except:
            print("List is shorter than the index!")
            return

        node = self.get_node(index-1)
        node.next = node.next.next
