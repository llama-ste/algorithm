from collections import deque

graph = {
    1: [2,3,4],
    2: [5],
    3: [5],
    4: [],
    5: [6,7],
    6: [],
    7: [3]
}


def bfs(start):
    visited = [start]
    deq = deque([start])

    while deq:
        node = deq.popleft()
        for adj in graph[node]:
            if adj not in visited:
                deq.append(adj)
                visited.append(adj)

    return visited


print(bfs(1))