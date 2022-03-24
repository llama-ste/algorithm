preGrid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","1"],
  ["0","0","1","1","0"]
]

# 재귀호출을 0,0부터 시작하여 진행 순서를 나열해 보았다.
# 0, 0에서 부터 top, bottom, left, right 순으로 움직이다.

# 0,0: top, bottom
# 1,0: top, bottom
# 2,0: top, bottom, left, right
# 2,1: top
# 1,1: top
# 0,1: top, bottom, left, right
# 0,2: top, bottom, left, right
# 0,3: top, bottom
# 1,3: top, bottom, left, right

# 1,3 까지 반복문을 돌고나면 추가 재귀호출이 없기 때문에 0,3 반복문으로 돌아가게된다.
# 이렇게 재귀호출은 처음 시작된 지점까지 다시 되돌아 가게된다.

endGrid = [
    ["0", "0", "0", "0"],
    ["0", "0", "0", "0"],
    ["0", "0"],
    ["0"],
]

class Solution:
    def dfs(self, grid, row, col):
        # 호출시 들어온 좌표에 있는 요소를 0으로 바꿔서 무한 재귀호출을 막아준다.
        grid[row][col] = '0'
        # 방향은 북, 남, 서, 동 순이다.
        directions = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
        # 북, 남, 서, 동 순으로 가져온다.
        for drow, dcol in directions:
            # drow,dcol이 0보다 작거나, len(grid)보다 크다면 grid 밖이므로 돌아가지 않는다.
            # 그리고 해당 grid[row][col]의 좌표에 1이어야 섬이기 때문에 섬일 경우에만 재귀호출을 한다.
            if drow >= 0 and dcol >= 0 and drow < len(grid) and dcol < len(grid[drow]) and grid[drow][dcol] == "1":
                # 재귀호출시 직전 반복문을 다 돌지 못하였다면 재귀호출 된것이 끝나면 다시 시작된다.
                self.dfs(grid, drow, dcol)

    def numIslands(self, grid):
        islands = 0

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                # 0, 0부터 시작된다.
                # 좌표에 1이 들어있다면 dfs를 호출하고, 재귀호출이 다 끝났을때 섬에 1을 더해준다.
                if grid[row][col] == "1":
                    # 재귀호출을 하기 때문에 grid를 인자로 주고 1을 0으로 바꿔서 무한 루프를 방지해준다.
                    self.dfs(grid, row, col)
                    islands += 1

        return islands

sol = Solution()

print(sol.numIslands(preGrid))


# class Solution:
#     BFS를 이용하여 풀어본 방식이다. (queue)
#     def island_bfs_queue(self, grid):
#         dx = [0, 0, 1, -1]
#         dy = [1, -1, 0, 0]
#         count = 0
#         rows, cols = len(grid), len(grid[0])
#
#         for row in range(rows):
#             for col in range(cols):
#                 if grid[row][col] != "1":
#                     continue
#
#                 count += 1
#
#                 queue = deque([(row, col)])
#
#                 while q:
#                     x, y = queue.popleft()
#                     grid[x][y] = "0"
#
#                     for i in range(4):
#                         new_x = x + dx[i]
#                         new_y = y + dy[i]
#
#                         if new_x >= 0 and new_y >= 0 and new_x < rows and new_y < cols and grid[new_x][new_y] == "1":
#                             grid[new_x][new_y] = "0"
#                             queue.append((new_x, new_y))
#
#         return count
#
#     DFS를 이용하여 풀어본 방식이다.
#     def island_dfs_stack(self, grid):
#         dx = [0, 0, 1, -1]
#         dy = [1, -1, 0, 0]
#         rows, cols = len(grid), len(grid[0])
#         cnt = 0
#
#         for row in range(rows):
#             for col in range(cols):
#                 if grid[row][col] != '1':
#                     continue
#
#                 cnt += 1
#                 stack = [(row, col)]
#
#                 while stack:
#                     x, y = stack.pop()
#                     grid[x][y] = '0'
#                     for i in range(4):
#                         nx = x + dx[i]
#                         ny = y + dy[i]
#                         if nx < 0 or nx >= rows or ny < 0 or ny >= cols or grid[nx][ny] != '1':
#                             continue
#                         stack.append((nx, ny))
#         return cnt