class Solution:
    def merge(self, intervals):
        # stack을 이용하여 조건이 완료된것만 쌓이게 해준다.
        stack = []
        for i in sorted(intervals):
            # 스택이 있고, 스택의 뒷자리 수가 다음 스택의 첫번째 자리보다 큰 경우
            # 같은 범위 안에 속하기 때문에 병합시켜준다.
            if stack and i[0] <= stack[-1][1]:
                # left는 스택에 쌓여있는게 정렬기준으로 이미 가장 작은 범위로 확정이므로 그대로 사용해준다.
                left = stack[-1][0]
                # right는 스택에 쌓인 요소와 현재 요소의 두번째 자리값을 비교하여 큰것을 사용해준다.
                # 위와 같이 한다면 두요소의 전체 범위를 잡아줄 수 있다.
                right = max(i[1], stack[-1][1])
                # 비교한 이전 스택을 빼준다.
                stack.pop()
                # 병합이 완료된 새 범위의 요소를 스택에 쌓아준다.
                stack.append([left, right])
            else:
                stack.append([i[0], i[1]])

        return stack


sol = Solution()
print(sol.merge([[1,3],[2,6],[8,10],[15,18]]))