preInput = "{()}"

class Solution:
    def isValid(self, s):
        stack = []

        opener = "{[("

        # Stack에 여는 괄호를 넣기 때문에 닫는 괄호가 들어 왔을때 stack의 top과 비교하기
        # 때문에 key를 닫는괄호로 넣고, val을 여는 괄호로 넣어서 동일한지 비교하게 된다.
        pair = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        stack = []

        for char in s:
            if char in opener:
                stack.append(char)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if pair[char] != top:
                    return False

        return not stack

sol = Solution()

print(sol.isValid(preInput))
# >>> True