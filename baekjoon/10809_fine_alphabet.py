import contextvars
import string
from pprint import pprint

s = "baekjoon"


# O(N)
def get_idx(word):
    result = [-1]*len(string.ascii_lowercase)
    for i in range(len(word)):
        # ord("a") -> 97 ...
        idx = ord(word[i]) - ord("a")
        if result[idx] == -1:
            result[idx] = i
    print(" ".join([str(num) for num in result]))


print("llama", "robin", sep=", ")

get_idx(s)


# O(N^2)
def get_idx_native(word):
    result = [-1] * len(string.ascii_lowercase)
    # i -> 0
    for i in range(len(word)):
        # char -> b
        char = word[i]
        # j -> 0
        for j in range(len(string.ascii_lowercase)):
            # lo -> a
            lo = string.ascii_lowercase[j]
            if result[j] == -1 and char == lo:
                result[j] = i
    print(" ".join([str(num) for num in result]))


get_idx_native(s)


# 알파벳 갯수찾기
ascii_arr = {}
for char in string.ascii_lowercase:
    ascii_arr[char] = s.count(char)
print(ascii_arr)


# text = 'hello, this is sparta'
#
# counter = {}
# # 21 번 연산
# for char in text:
#     if not char.isalpha():
#         continue
#     if char in counter:
#         counter[char] += 1
#     else:
#         counter[char] = 1
# pprint(counter)
#
# a = [3, 5, 6, 1, 2, 4]
#
#
# def is_num_exist(num,arr):
#     for ele in arr:
#         if num == ele:
#             return True
#     return False
#
#
# print(is_num_exist(10, a))