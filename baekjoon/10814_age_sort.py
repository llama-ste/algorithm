from sys import stdin
input = stdin.readline

n = int(input())

li = [input().split(" ") for _ in range(n)]

li.sort(key=lambda x: int(x[0]))

for i in range(n):
    print(li[i][0], li[i][1], end="")