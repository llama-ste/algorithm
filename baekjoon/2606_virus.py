n = int(input())
m = int(input())

# graph = [
#     [],
#     [2, 5],
#     [1, 3, 5],
#     [2],
#     [7],
#     [1, 2, 6],
#     [5],
#     [4]
# ]

# 인데스는 0부터 시작하지만 start를 1로 시작하기 때문에 하나더 만들어 주는 것이다.
graph = [[] * n for _ in range(n+1)]

# m개의 간선수를 받아서 graph에 경로를 담아준다.
for _ in range(m):
    a, b = map(int, (input().split()))
    graph[a].append(b)
    graph[b].append(a)

# 인데스는 0부터 시작하지만 start를 1로 넣기때문에 하나더 만들어 주는 것이다.
visited = [0] * (n+1)


def dfs(start):
    # start가 들어온다면 방문한것을 표시하기위해 1로 바꿔준다.
    visited[start] = 1
    # graph의 1번에서 연결된 노드들의 요소를 순회한다.
    for i in graph[start]:
        # 방문하지 않았다면 재귀호출하여 방문처리를 해주고, 방뭇할수 있는곳을 다 순회한다면
        # if문을 더이상 타지 않기 때문에 재귀함수도 종료된다.
        if visited[i] == 0:
            dfs(i)


dfs(1)

# 1번을 통하여 감염된 수를 구하는 것이기 때문에 시작점인 1을 빼주는 것이다.
print(sum(visited) - 1)
