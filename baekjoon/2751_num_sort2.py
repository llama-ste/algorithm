import heapq
from sys import stdin
input = stdin.readline

n = int(input())

li = [int(input()) for _ in range(n)]

li.sort()

for elem in li:
    print(elem)

# heap = []
#
# for _ in range(n):
#     heapq.heappush(heap, int(input()))
#
# for _ in range(n):
#     print(heapq.heappop(heap))