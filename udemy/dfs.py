graph = {
    1: [2,3,4],
    2: [5],
    3: [5],
    4: [],
    5: [6,7],
    6: [],
    7: [3]
}


def dfs(start, visited):
    visited.append(start)

    for adj in graph[start]:
        if adj not in visited:
            dfs(adj, visited)

    return visited


print(dfs(1, []))