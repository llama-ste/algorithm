import heapq
from sys import stdin

input = stdin.readline

# 1번 풀이 방법
pq = []

for _ in range(int(input())):
    num = int(input())

    if num == 0:
        # 0이 들어오고, pq가 비어있지 않다면 pop하여 보여주고, 비었다면 0을 보여준다.
        print(heapq.heappop(pq)[1] if pq else 0)
    else:
        # 절대값을 튜플을 이용하여 첫번째 인자로 넣어서 절대값이 작은 애들로 정렬되게 만들어준다.
        # 이렇게 되면 절대값도 가장 작고, 들어온 숫자도 가장 작은 순으로 정렬되게 된다.
        heapq.heappush(pq, [abs(num), num])

# 2번 풀이 방법
# min_heap = [] # 양수
# max_heap = [] # 음수 값을 넣을때 -를 붙어서 양수로 바꿔서 넣고, 뺄때 값을 이용하려면 다시 -를 붙여서 원복한다.
#
# for _ in range(int(input())):
#     num = int(input())
#
#     if num == 0:
#         if min_heap and max_heap:
#             # 음수를 양수 처리하여 들어갔기 때문에 절대값으로 만들어주지 않아도 절대값이다.
#             if min_heap[0] < max_heap[0]:
#                 print(heapq.heappop(min_heap))
#             else:
#                 # 원래값은 음수이기 때문에 원복시켜 준것이다.
#                 print(-heapq.heappop(max_heap))
#         elif min_heap:
#             print(heapq.heappop(min_heap))
#         elif max_heap:
#             # 원래값은 음수이기 때문에 원복시켜 준것이다.
#             print(-heapq.heappop(max_heap))
#         else:
#             print(0)
#     else:
#         if num > 0:
#             heapq.heappush(min_heap, num)
#         else:
#             # 음수일때 -를 붙여서 양수로 들어가게 만들어 max_heap을 만들어 준다.
#             heapq.heappush(max_heap, -num)
