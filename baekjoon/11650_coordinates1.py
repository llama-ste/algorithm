from sys import stdin
input = stdin.readline

num = int(input())

coordinates = [list(map(int, input().rstrip().split(" "))) for _ in range(num)]

coordinates.sort(key=lambda x: (x[0], x[1]))

for i in range(len(coordinates)):
    print(coordinates[i][0], coordinates[i][1])