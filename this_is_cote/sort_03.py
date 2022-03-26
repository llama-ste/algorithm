# 성적이 낮은 순서로 학생 출력하기
# 모든 학생의 이름을 성적이 낮은 순서대로 출력한다.
# 첫번째 줄에 학생수 N이 입력되고, 두번째줄부터 학생수만큼 이름, 성적이 공백으로 구분되어 출력된다.
# 2
# 홍길동 95
# 이순신 77

from sys import stdin

input = stdin.readline

# 학생수를 입력 받는다.
nums = int(input())

lst = []

for i in range(nums):
    # 이름과 점수를 따로 변수에 담아준다.
    name, score = input().split()
    # 점수를 인덱스0에 넣어서 정렬하기 쉽게 만들어준다.
    lst.append([int(score), name])

# index0을 기준으로 정렬된다.
lst.sort()

for i in lst:
    # 리스트를 돌면서 이름만 출력해주면 되고, 한줄에 출력이기 때문에 end에 공백을 넣어줬다.
    print(i[1], end=" ")

print(lst)
# 학생수만큼 반복문을 돌려준다.
# for i in range(nums):
#     # 이름과 점수를 따로
#     name, score = input().split()
#     lst.append([name, int(score)])
#
# res2 = sorted(lst, key=(lambda x: x[1]))
#
# for i in res2:
#     print(i[0], end=" ")

# dic = {}
#
# for _ in range(nums):
#     name, score = input().split()
#     dic[name] = int(score)
#
# res = sorted(dic.items(), key=(lambda x: x[1]), reverse=True)
#
# for i in res:
#     print(i[0], end=" ")