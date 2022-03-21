N, L = map(int, input().split())
# 방법 1
coordinate = sorted(list(map(int, input().split())))
# 물이 새는곳에서 부터 출발하기 때문에 count를 1부터 시작해준다.
count = 1

# 시작점이다.
start = coordinate[0]

# 구멍이 뚫린 수만큼만 반복문이 돌면 된다.
for i in range(N):
    # 시작점 + 테이프 길이를 했을때, 다음 지점보다 크다면 수리할곳이 없기때문에 다음 반복문으로 넘어간다.
    if start + L > coordinate[i]:
        continue
    # 조건문을 통과하지 못하였다면 시작점을 해당 위치로 옮기고 테이프를 붙이기 때문에 카운트를 올려준다.
    start = coordinate[i]
    count += 1

print(count)

# 방법 2 - 조건이 커진다면 시간초과 할 수 있다.
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