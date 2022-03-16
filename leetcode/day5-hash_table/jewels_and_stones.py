import collections

preJewels = "aA"
preStones = "aAAbbbb"


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # stone을 Counter로 중복되는 요소를 합쳐서 카운팅한다.
        res = collections.Counter(stones)

        # jewels의 보석을 빼서, res[key]로 사용하면 카운팅된 개수가 나오기 때문에 sum()으로 리스트 요소를 합치면 보석의 갯수를 찾을 수 있다.
        return sum([res[k] for k in jewels])


sol = Solution()

print(sol.numJewelsInStones(preJewels, preStones))