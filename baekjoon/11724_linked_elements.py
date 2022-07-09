# N×(N-1)/2) == nC2
from sys import stdin

input = stdin.readline

N, M = map(int, input().split())

grid = [[0] * N for _ in range(N)]

for _ in range(M):
    a, b = map(lambda x: x -1, map(int, input().split()))
    grid[a][b] = grid[b][a] = 1

check = [False] * N
answer = 0


def dfs(start):
    for nextNode in range(N):
        if grid[start][nextNode] and not check[nextNode]:
            check[nextNode] = True
            dfs(nextNode)


for i in range(N):
    if not check[i]:
        answer += 1
        check[i] = True
        dfs(i)

print(answer)