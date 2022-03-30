from sys import stdin
import heapq

input = stdin.readline

num = int(input())

min_heap = []

for _ in range(num):
    ele = int(input())

    # ele가 0이고 힙이 없다면 0을 프린터 한뒤 다음 반복문으로 넘어간다.
    if ele == 0 and not min_heap:
        print(0)
        continue
    # ele가 0일때 힙에서 가장 작은 값을 빼고, 프린트한다.
    # python의 heapq는 기본적으로 min heap으로 만들어졌다.
    # heappop을 하면 가장 작은값을 빼준다.
    if ele == 0:
        print(heapq.heappop(min_heap))
        continue

    # ele가 0이 아니라면 힙에 요소를 넣어준다. (min_heap으로 자동 정렬된다.)
    heapq.heappush(min_heap, ele)


# 문제의 입력값
# 9
# 0
# 12345678
# 1
# 2
# 0
# 0
# 0
# 0
# 32