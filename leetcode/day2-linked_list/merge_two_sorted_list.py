class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

class Solution:
    def mergeTwoLists(self, list1, list2):
        # dummy와 현재 head로 이용할 노드 2개를 만들어 두는게 핵심이다.
        curr = dummy = ListNode()

        # list가 둘다 있다면 더 적은 val를 기준으로 next를 옮겨 나간다.
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        # 두개의 리스트중 하나가 먼저 None에 도달하기 때문에 while문이 종료된 뒤 아래와 같이 만든것이다.
        curr.next = list1 or list2

        # dummy.next는 병합된 연결 리스트의 head와 연결되어 있다.
        return dummy.next

sol = Solution()

print(sol.mergeTwoLists(l1, l2))