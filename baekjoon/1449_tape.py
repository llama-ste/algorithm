N, L = map(int, input().split())

# 물이 새는 곳이 1000보다 작거나 같다고 하였기 때문에 0~1000까지 1001개를 만들었다.
bools = [False] * 1001
# 물이 새는곳의 좌표를 받아둔다.
coordinates = list(map(int, input().split()))

# 물이 새는곳을 True로 만들어 준다.
for i in coordinates:
    bools[i] = True

# 테이프 사용 개수를 선언해둔다.
used = 0

# 모든 위치를 순회하기 위한 좌표이다.
x = 0

while x < 1001:
    # True라면 뚫린곳이기 때문에 테이프를 사용해야 한다.
    if bools[x]:
        used += 1
        # 테이프의 길이 내에 뚫린곳이 있다면 한번의 사용으로 막기 때문에 테이프의 길이만큼 건너뛴다.
        x += L
    else:
        # 뚫린곳을 발견할 때까지 하나씩 순회 하는것이다.
        x += 1

# 총 사용 개수를 출력하면 정답이 나온다.
print(used)