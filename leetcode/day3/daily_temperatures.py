preInput = [73, 74, 75, 71, 69, 72, 76, 73]


class Solution:
    def dailyTemperatures(self, temperatures):
        answer = [0] * len(temperatures)
        stack = []

        # index를 요일로 이용한다.
        for today_day, today_temp in enumerate(temperatures):
            # stack이 있고, stack의 요일보다 오늘온도가 높다면 실행된다.
            while stack and temperatures[stack[-1]] < today_temp:
                # stack의 요일을 빼고, 오늘날과 비교해 걸린 시간을 답에 넣어준다.
                past_day = stack.pop()
                answer[past_day] = today_day - past_day
            stack.append(today_day)

        return answer


sol = Solution()

print(sol.dailyTemperatures(preInput))
# >>> [1, 1, 4, 2, 1, 1, 0, 0]