from sys import stdin
import heapq

input = stdin.readline

num = int(input())
max_heap = []

for _ in range(num):
    ele = int(input())

    if ele == 0 and not max_heap:
        print(0)
        continue

    if ele == 0:
        print(heapq.heappop(max_heap)[1])
        continue
    # heapq는 기본적으로 minHeap으로 동작하는데, 이것을 응용한 것이다.
    # 튜플을 넣어서 맨앞의 값을 기준으로 최소힙이 구성되는 원리를 이용한것이다.
    # 첫번째 인자에 -element를 하면 가장 큰값이 젤앞으로 오게 되기때문에 maxHeap을 구성할 수 있다.
    heapq.heappush(max_heap, (-ele, ele))