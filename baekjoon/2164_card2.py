from collections import deque

nums = int(input())

# range의 두번째 인자는 해당 숫자의 앞까지 자르기 때문에 +1을 해준다.
# range를 이용하면 배열로 나오기 때문에 반복문을 돌 필요도 없다.
# deque를 이용하면 popleft(), appendleft()가 사용가능하다 - 시간복잡도 O(1)
deq = deque(range(1, nums + 1))

while len(deq) > 1:
    # deq[0]을 빼고, 그다음 deq[0]을 젤 뒤로 보내는 것이다.
    deq.popleft()
    deq.append(deq.popleft())

print(deq.pop())