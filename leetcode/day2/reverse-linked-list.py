class Node:
    def __init__(self, data=0, next=None):
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


dummy = [1, 2, 3, 4, 5]

linked = LinkedList()

for i in dummy:
    linked.append(i)

preHead = linked.head

# 1. node=head, prev=None을 만들고 node가 있다면 next=node.next로 방향을 바꾸기전 데이터를 저장해둔다.
# 2. node.next=prev로 방향을 뒤집고, prev는 현재의 node로 node는 1번에서 저장해둔 next로 바꿔준다.
# 3. node가 존재할때까지 반복한다면 prev가 head가 된다.
class Solution:
    def reverseList(self, head):
        node, prev = head, None
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        return prev


sol = Solution()

result = sol.reverseList(preHead)

print(preHead.data, result.data) # => 1, 5