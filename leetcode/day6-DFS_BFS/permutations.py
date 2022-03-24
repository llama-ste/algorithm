preInput = [1, 2, 3]


class Solution:
    def __init__(self):
        self.res = []

    def permute(self, nums):
        # DFS 함수로 nums와 결과를 담을 빈 배열을 넣어준다.
        self.backtrack(nums, [])
        return self.res

    def backtrack(self, nums, path):
        # nums가 다빠졌다면 순열이 완성된것이기 때문에 result에 담아준다.
        if not nums:
            self.res.append(path)

        # 재귀호출을 하는데 헷갈리기 쉽기 때문에 결과물을 순차적으로 아래에 주석처리 해두었다.
        for x in range(len(nums)):
            self.backtrack(nums[:x] + nums[x + 1:], path + [nums[x]])
        # nums = [1,2,3]  x = 0
        # nums[:x] => []  nums[x+1:] => [2, 3]  nums[x] => [1]
        # nums = [2, 3]  x = 0
        # nums[:x] => [] nums[x+1:] => [3] nums[x] => [2]zX
        # nums = [3]  x = 0
        # nums[:x] => [] nums[x+1:] => [] nums[x] => [3]


sol = Solution()
print(sol.permute(preInput))

# dfs(nums = [1, 2, 3] , path = [] , result = [] )
# |____ dfs(nums = [2, 3] , path = [1] , result = [] )
# |      |___dfs(nums = [3] , path = [1, 2] , result = [] )
# |      |    |___dfs(nums = [] , path = [1, 2, 3] , result = [[1, 2, 3]] ) # added a new permutation to the result
# |      |___dfs(nums = [2] , path = [1, 3] , result = [[1, 2, 3]] )
# |           |___dfs(nums = [] , path = [1, 3, 2] , result = [[1, 2, 3], [1, 3, 2]] ) # added a new permutation to the result
# |____ dfs(nums = [1, 3] , path = [2] , result = [[1, 2, 3], [1, 3, 2]] )
# |      |___dfs(nums = [3] , path = [2, 1] , result = [[1, 2, 3], [1, 3, 2]] )
# |      |    |___dfs(nums = [] , path = [2, 1, 3] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3]] ) # added a new permutation to the result
# |      |___dfs(nums = [1] , path = [2, 3] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3]] )
# |           |___dfs(nums = [] , path = [2, 3, 1] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1]] ) # added a new permutation to the result
# |____ dfs(nums = [1, 2] , path = [3] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1]] )
#        |___dfs(nums = [2] , path = [3, 1] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1]] )
#        |    |___dfs(nums = [] , path = [3, 1, 2] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2]] ) # added a new permutation to the result
#        |___dfs(nums = [1] , path = [3, 2] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2]] )
#             |___dfs(nums = [] , path = [3, 2, 1] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]] ) # added a new permutation to the result