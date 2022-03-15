from collections import  deque

# preInput = int(input())
preInput = 100


def sol(num):
    # range의 두번째 인자는 해당 숫자의 앞까지 자르기 때문에 +1을 해준다.
    # deque를 이용하면 popleft(), appendleft()가 사용가능하다 - 시간복잡도 O(1)
    deq = deque([i for i in range(1, num+1)])
    while len(deq) > 1:
        # deq[0]을 빼고, 그다음 deq[0]을 젤 뒤로 보내는 것이다.
        deq.popleft()
        deq.append(deq.popleft())
    return deq.popleft()


print(sol(preInput))