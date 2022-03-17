progresses = [100, 70, 55]
speeds = [1, 30, 5]

def solution(progress, speed):
    answer = []
    # 시간을 일수로 사용하여 와일문을 한바퀴 돌때마다 1씩 더해준다.
    # 다음 프로그래스가 오더라도 time*speed로 100이 넘으면 바로 빠질 수 있게 해준다.
    time = 0
    # count는 밀린 작업이 한번에 빠질 경우 카운팅 해야되기 때문에 선언한다.
    count = 0

    while len(progress) > 0:
        if progress[0] + time * speed[0] >= 100:
            progress.pop(0)
            speed.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1

    answer.append(count)

    return answer

print(solution(progresses,speeds))