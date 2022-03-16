from collections import Counter

preInput = [1, 1, 1, 2, 2, 3]
pre = 2


class Solution:
    def topKFrequent(self, nums, k):
        # Counter()를 이용하면 배열의 중첩된 요소를 카운팅하여 딕셔너리로 반환해준다.
        # key는 중첩된 요소, value는 중첩된 개수가 들어있다.
        # most_common()를 이용하면 중첩이 많은 순으로 정렬되고 인자를 넣는다면 가장 많은 순서대로 인자만큼 끊어서 보여준다.
        most = Counter(nums).most_common(k)

        result = []

        # [(k, v), (k, v)]로 담겨있기 때문에 for문을 이용하여 key만 사용했다.
        for key, value in most:
            result.append(key)

        return result


sol = Solution()

print(sol.topKFrequent(preInput, pre))