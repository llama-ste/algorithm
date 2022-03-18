graph = [
    [0,1,1,0,1,0,0],
    [0,1,1,0,1,0,1],
    [1,1,1,0,1,0,1],
    [0,0,0,0,1,1,1],
    [0,1,0,0,0,0,0],
    [0,1,1,1,1,1,0],
    [0,1,1,1,0,0,0],
]

# 아래는 백준에서 입력값을 받는 것이다.
# n = int(input())
# graph = []
#
# for i in range(n):
#     graph.append(list(map(int, input())))

# 아파트 단지를 세기위한 카운터를 외부에 선언하였다.
# dfs에서 grid[x][y] == 1 일때 1씩 더하고, 재귀가 종료 되었을때도 1을 더해준다.
count = 0


class Solution:
    def dfs(self, grid, row, col):
        # global로 count를 가져와서 더할수 있게 만들어준다.
        global count
        # 방문한 곳은 0으로 바꿔줘서 무한 재귀호출이 되지 않게 만들어준다.
        grid[row][col] = 0
        # 북 남 서 동 순으로 들어있다.
        directions = [[row-1, col], [row+1, col], [row, col-1], [row, col+1]]

        # 북 남 서 동 순으로 확인한뒤 움직인다.
        # 반복문 도중에 재귀호출이 될 경우, 마지막 재귀 호출이 종료될 때부터 역순으로 남은 반복문이 실행된다.
        for drow, dcol in directions:
            if drow >= 0 and dcol >= 0 and drow < len(grid) and dcol < len(grid[drow]) and grid[drow][dcol] == 1:
                # 연결된 집의 수를 세기 위한 것이다.
                count += 1
                self.dfs(grid, drow, dcol)

    def numIsApartment(self, grid):
        # 아파트 단지 수를 세기 위한 변수다.
        aprtment = 0
        # 여러 단지가 존재한다면 한 단지의 탐색이 끝나면 집의 수를 어딘가에 담아두고 카운터를 초기화해야 되기 때문에 선언했다.
        counts = []
        global count

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    self.dfs(grid, row, col)
                    # dfs 함수에서는 첫집을 제외한 이후 발견되는 집을 카운팅 하기 때문에 첫집의 카운트를 더해준다.
                    count += 1
                    # dfs가 종료된다면 연결된 노드가 없다는것이기 더이상 없다는 것이기때문에 단지수를 더해준다.
                    aprtment += 1
                    # 다음 구역에서 다시 0부터 세야하기 때문에 배열에 담고 0으로 초기화해준다.
                    counts.append(count)
                    count = 0

        return aprtment, counts


sol = Solution()

a, b = sol.numIsApartment(graph)
b.sort()

print(a)
for i in range(len(b)):
    print(b[i])