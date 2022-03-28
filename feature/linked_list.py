class Node:
    # 노드는 아이템과 다음 아이템을 가리키는 포인터가 있다.
    def __init__(self, item, next=None):
        self.item = item
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, item):
        # head가 없다면 head에 첫 노드를 만들어 준다.
        if self.head is None:
            self.head = Node(item, None)
            return

        node = self.head
        # node.next가 None일때 까지 node.next를 현재 node로 바꿔준다.
        while node.next:
            node = node.next

        # node.next가 None이라면 tail이기 때문에 해당 위치에서 노드를 만들어 준다.
        node.next = Node(item, None)

    def get_node(self, index):
        if self.head is None:
            print("List is empty!")
            return None

        # head의 위치를 인덱스 0으로 잡고 현재 인덱스를 0으로 만들고, head도 변수에 담아준다.
        curr = 0
        node = self.head

        # index가 0이라면 head이기 때문에 그대로 반환시켜준다.
        if index == 0:
            return node

        try:
            # 현재 인덱스가, 받아온 인덱스보다 작을때 까지 node.next를 현재 노드로 만들어서 반환해준다.
            while curr < index:
                curr += 1
                node = node.next
            return node
        except:
            # 만약 받아온 인덱스에 도달하기전에 node.next가 None이 된다면 에러 처리를 해준다.
            print("List is shorter than the index!")
            return

    def add_node(self, index, item):
        # 새 노드를 바로 만들어둔다.
        new_node = Node(item, None)

        # 인덱스가 0이라면 새 노드의 넥스트를 헤드로 만들고, 헤드를 새 노드로 만들어준다.
        # 헤드가 없는 상태였어도 새 노드의 넥스트에 None이 들어가고 새 노드가 헤드가 되기 때문에 정상 동작한다.
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        # 삽입할 위치 바로 전 노드를 잡아와야 한다.
        # 삽입할 위치 바로 전 노드를 잡아와서 삽입될 위치의 기존 노드를 저장해둔뒤 node.next를 바꿔야한다.
        node = self.get_node(index - 1)

        # 받아온 인덱스보다 연결리스트의 길이가 짧더라면 None이 반환되기 때문에 그대로 끝내준다.
        if node is None:
            return
        # 노드는 있는데 node.next가 None이라면 현재 위치가 tail이기 때문에 node.next에 새 노드를 넣어 tail로 만들어준다.
        elif node.next is None:
            node.next = new_node
            return

        # 삽입될 위치의 노드를 저장해둔다.
        next_node = node.next
        # 바로 전 노드의 넥스트를 새 노드로 바꿔준다.
        node.next = new_node
        # 새 노드의 넥스트를 기존 삽입될 위치의 노드로 다시 연결시켜주면 완료된다.
        new_node.next = next_node

    def delete_node(self, index):
        if self.head is None:
            print("List is empty!")
            return

        # 받아온 인덱스가 0이라면 헤드를 헤드의 넥스트로 이동시켜준다.
        if index == 0:
            self.head = self.head.next
            return

        # 삭제될 위치의 바로 전 노드를 가져와야한다.
        # 삭제될 위치를 건너뛰고 다음 노드랑 연결시켜줘야되기 때문이다.
        node = self.get_node(index - 1)

        # 노드가 없다면 삭제될 위치보다 연결리스트의 길이가 짧은것이다.
        if node is None:
            return
        # 노드는 있는데 node.next가 None이라면 tail이기 때문에 이경우에도 연결리스트의 길이가 짧은것이다.
        elif node.next is None:
            print("List is shorter than the index!")
            return

        # 조건문을 다 통과하였다면 node.next를 다음 다음으로 넘겨서 삭제될 위치의 데이터를 유실시킨다.
        node.next = node.next.next


lst = LinkedList()

lst.append(3)
lst.add_node(1, 5)
print(lst.get_node(1).item)