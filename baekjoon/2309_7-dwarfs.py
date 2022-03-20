# brute force 방법이다. (7개의 합을 구하는것이기 때문에 2개를 빼서 구하는것도 방법이다.)
# 반복문의 range()에 유의한다. (i가 끝까지 간다면 j는 없는것이다.)
heights = [int(input()) for _ in range(9)]
heights.sort()
total = sum(heights)


def f():
    for i in range(8):
        for j in range(i + 1, 9):
            if total - heights[i] - heights[j] == 100:
                for k in range(9):
                    if k != i and k != j:
                        print(heights[k])
                return


f()

# 파이썬 내장 모듈로 간단하게 풀어본 방법이다. (알고리즘 문제를 풀때는 적합하지 않다.)
# from itertools import combinations
#
# heights = [int(input()) for _ in range(9)]
#
# for combi in combinations(heights, 7):
#     if sum(combi) == 100:
#         for height in sorted(combi):
#             print(height)
#         break