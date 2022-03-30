import heapq
from sys import stdin

input = stdin.readline

num = int(input())

deck = []
for _ in range(num):
    heapq.heappush(deck, int(input()))

# 카드 덱이 1개라면 비교할게 없기 때문에 0을 프린트하고 끝내준다.
if len(deck) == 1:
    print(0)
else:
    answer = 0
    # 반복문 시점의 최소합을 더해가면 결과도 최소가 나오게 된다. (Greedy)
    while len(deck) > 1:  # 마지막에 합산 결과를 힙에 다시 넣기 때문에 1개만 남는다면 계산이 끝난것이다.
        # python heapq는 기본적으로 minheap이기 때문에 가능한 풀이방법이다.
        min_1 = heapq.heappop(deck)
        min_2 = heapq.heappop(deck)
        answer += min_1 + min_2  # 제일 작은 덱 두개를 더해준다.
        # 항상 최소 카드덱으로 구해야되기 때문에 더해진 카드덱도 minheap으로 정렬시켜 줘야한다.
        heapq.heappush(deck, min_1 + min_2)

    print(answer)