preInput = [73, 74, 75, 71, 69, 72, 76, 73]


class Solution:
    def dailyTemperatures(self, temperatures):
        answer = [0] * len(temperatures)
        stack = []

        for today_day, today_temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < today_temp:
                past_day = stack.pop()
                answer[past_day] = today_day - past_day
            stack.append(today_day)

        return answer


sol = Solution()

print(sol.dailyTemperatures(preInput))
# >>> [1, 1, 4, 2, 1, 1, 0, 0]