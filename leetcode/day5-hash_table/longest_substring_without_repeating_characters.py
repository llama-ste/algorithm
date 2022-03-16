class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 같은 문자를 반복하지 않게, 이미 나온 문자라면 딕셔너리의 key에 문자를 value에 인덱스를 담는다.
        # 인덱스는 문자열 시작 위치를 파악하여 같은 문자가 나온다면 처음 나온 위치 +1로 시작 지점을 변경해줘야 한다.
        used = {}
        max_length = start = 0

        for index, char in enumerate(s):
            # if val in dict는 자주 사용되는 방법이다.
            # 일반적으로 이미 존재한다면 수를 늘려가는데, 여기서는 시작 지점을 늘려가는 것이다.
            if char in used and start <= used[char]:
                # 문자가 겹치면 안되기 때문에 이전의 위치 +1을하여야 현재 최대 길이를 구할 수 있는것이다.
                start = used[char] + 1
            else:
                # 기존의 최대 길이와 새로운 문자가 나왔을때 index - start + 1을 비교하여 더 높은게 제일 긴것이다.
                max_length = max(max_length, index - start + 1)
            # 반복문을 돌 때마다 문자의 위치를 최신화 시켜줘야 시작지점부터 끝나는곳 까지의 길이를 정확히 알 수 있다.
            used[char] = index

        return max_length


sol = Solution()

print(sol.lengthOfLongestSubstring("abcabcbb"))