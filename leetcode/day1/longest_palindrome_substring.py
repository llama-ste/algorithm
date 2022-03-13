# 팰린드롬은 거꾸로 읽어도 제대로 읽는것과 같은 문장등을 의미한다.
import collections
import re

preInput = "babad"


class Solution:
    def longestPalindrome(self, s):
        result = ""
        resultLength = 0

        #해당 사항이 없을 경우 빠르게 return한다.
        if len(s) < 2 or s == s[::-1]:
            return s

        for i in range(len(s)):
            # odd length
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > resultLength:
                    result = s[left:right + 1]
                    resultLength = right - left + 1
                left -= 1
                right += 1

            # even length
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > resultLength:
                    result = s[left:right + 1]
                    resultLength = right - left + 1
                left -= 1
                right += 1

        return result

sol = Solution()

print(sol.longestPalindrome(preInput))

# 팰린드롬 체크하는 3가지 방법
# st = "A man, a plan, a canal: Panama"
#
# # List 이용  pop(0)은 시간복잡도가 O(N)이다.
# strs = []
# def isPalindromeCheck(s):
#     for char in s:
#         if char.isalnum():
#             strs.append(char.lower())
#
#     while len(strs) > 1:
#         if strs.pop(0) != strs.pop():
#             return False
#
#     return True
#
#
# # Deque이용  popleft()는 시간복잡도가 O(1)이다.
# def isPalindromeCheckOne(s):
#     str = collections.deque()
#
#     for char in s:
#         if char.isalnum():
#             str.append(char.lower())
#
#     while len(str) > 1:
#         if str.popleft() != str.pop():
#             return False
#
#     return True
#
# 표현식을 이용하여 소문자 알파벳으로만 비교하여 체크하기
# def isPalindromeCheckTwo(s):
#     p = s.lower()
#     p = re.sub('[^a-z0-9]', '', s)
#     return s == s[::-1]