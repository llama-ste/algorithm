from sys import stdin, stdout
# 입력 출력을 가속화 한것이다.
input = stdin.readline
print = stdout.write

N, M = map(int, input().split())
sites = {}

# input으로 받는 site, password를 딕셔너리에 key: value로 저장한다.
for _ in range(N):
    site, password = input().split(" ")
    sites[site] = password

# input으로 받는 원하는 site를 키로 넣어 비밀번호를 출력한다.
for _ in range(M):
    print(sites[input().rstrip()])