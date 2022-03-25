import heapq


# 간단한 해결방법
class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        # heapq에 있는 구현된 기능을 이용하였다.
        return heapq.nlargest(k, nums)[-1]


# 힙을 직접 구현하여서 해결하는 방법
class BinaryMaxHeap:
    def __init__(self):
        self.items = [None]

    def __len__(self):
        return len(self.items) - 1

    def _percolate_up(self):
        curr = len(self)
        parent = curr // 2

        while parent > 0:
            if self.items[curr] > self.items[parent]:
                self.items[curr], self.items[parent] = self.items[parent], self.items[curr]

            curr = parent
            parent = curr // 2

    def _percolate_down(self, curr):
        biggest = curr
        left = 2 * curr
        right = 2 * curr + 1

        if left <= len(self) and self.items[left] > self.items[biggest]:
            biggest = left

        if right <= len(self) and self.items[right] > self.items[biggest]:
            biggest = right

        if biggest != curr:
            self.items[curr], self.items[biggest] = self.items[biggest], self.items[curr]
            self._percolate_down(biggest)

    def insert(self, k):
        self.items.append(k)
        self._percolate_up()

    def extract(self):
        if len(self) < 1:
            return None

        root = self.items[1]
        self.items[1] = self.items[-1]
        self.items.pop()
        self._percolate_down(1)

        return root


def find_kth_largest(k, lst):
    max_heap = BinaryMaxHeap()

    # list에 있는 아이템을 다 힙에 넣어준다.
    # 이때 insert에서 percolate_up을 호출하여 큰 순서대로 노드 위치 이동을 시켜준다.
    for ele in lst:
        max_heap.insert(ele)

        # 루트노드를 k번 만큼 추출한뒤 가장 마지막을 가져오면 k번째 큰것이기 때문에 정답이나온다
    return [max_heap.extract() for _ in range(k)][-1]


num_list = [4,2,9,1,3,6,8,4,34]
num = 3

print(find_kth_largest(num, num_list))