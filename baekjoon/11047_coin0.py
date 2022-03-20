N, K = map(int, input().split())

# 큰 단위의 동전부터 사용하기 위하여 reverse()를 이용한다.
coins = [int(input()) for _ in range(N)]
coins.reverse()

count = 0
for coin in coins:
    # 동전단위 보다 구해야 하는 값이 높을때 현재 사용할 수 있는 최대 금액의 동전 인것이다.
    if K >= coin:
        # 현재 동전으로 구하는 금액을 나눠서 몫을 카운팅한다
        count += K // coin # => 4 (1000원)
        # 구하는 금액에서 몫만큼의 값을 빼고 나머지를 구한다.
        # 나머지가 다음 단계에서 구해야 하는 값이 되는것이다.
        K %= coin # => 4200 % 1000 = 200 , 4

print(count)