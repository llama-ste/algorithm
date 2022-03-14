# Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn)
# such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.

preInput = [1, 4, 3, 2]

# 오름차순으로 정렬한 뒤, 슬라이싱 기능으로 짝수번만 더해준다. (입력값이 홀수라면 내림차순을 이용해야한다.)
# min()을 최대 값으로 만들어 낼 수 있는 방법이다.
class Solution:
    def arrayPairSum(self, nums):
        return sum(sorted(nums)[::2])

sol = Solution()

print(sol.arrayPairSum(preInput))
