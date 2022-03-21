from sys import stdin
from itertools import combinations
input = stdin.readline

a, b = map(int, input().split())

password = input().split()
password.sort()

# 정렬된 문자를 combinations 모듈을 이용하여 입력값 크기의 조합으로 만들어 준다.
combi = list(combinations(password, a))

# 모음이 한자 이상 포함되야 하기 때문에 모음을 만들어 줬다.
vowels = "aeiou"

# 조합을 반복문을 돌린다.
for ele in combi:
    # 반복문안에서 자음 모음 카운터를 만들어서 반복문 마다 카운터가 초기화되게 만들어 준다.
    vowCount = conCount = 0
    for char in ele:
        # 요소에서 모음이 있다면 모음 카운터를 올려주고 아니라면 자음 카운터를 올린다.
        if char in vowels:
            vowCount += 1
        else:
            conCount += 1
    # 반복문이 종료되고 문제가 요구하는 카운터에 적합한 비밀번호만 프린트한다.
    if vowCount >= 1 and conCount >= 2:
        print("".join(ele))
