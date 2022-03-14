import collections

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# => 입력받은 배열을 같은 애너그램끼리 그룹화 시킨다.

preInput = ["eat","tea","tan","ate","nat","bat"]

class Solution:
    def groupAnagrams(self, strs):
        # 존재하지 않는 키에 삽입하는 경우 KeyError가 나는것을 방지하기 위해 초기값을 할당해준다.
        # 기본값이 list이기 때문에 append가 사용가능 하다.
        anagrams = collections.defaultdict(list)

        for word in strs:
            # dict에 정렬된 단어를 키로 넣고, 값으로 원래 단어를 넣는다.
            anagrams["".join(sorted(word))].append(word)

            # List 길이순으로 정렬해줬다.
        return sorted(list(anagrams.values()), key=len)

sol = Solution()

print(sol.groupAnagrams(preInput))