from sys import stdin
from collections import deque, defaultdict

input = stdin.readline

vertex, edge, start = map(int, input().split())

graph = [[0] * (vertex + 1) for _ in range(vertex + 1)]

for _ in range(edge):
    row, col = map(int, input().split())

    graph[row][col] = graph[col][row] = 1


def bfs(star):
    visited = [star]

    que = deque([])
    que.append(star)

    while que:
        ro = que.popleft()

        for co in range(len(graph[0])):
            if graph[ro][co] == 1 and co not in visited:
                visited.append(co)
                que.append(co)

    return visited


print(" ".join(map(str, bfs(start))))


def dfs(star, visited=[]):
    visited.append(star)

    for co in range(len(graph[0])):
        if graph[star][co] == 1 and co not in visited:
            dfs(co, visited)
    return visited

print(" ".join(map(str, dfs(start))))