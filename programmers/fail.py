from collections import Counter


def solution(n, stages):
    answer = {}
    # 실패율을 구하는것이기 때문에 사람수를 미리 구해둔다.
    people = len(stages)
    # 스테이지별 사람을 미리 카운팅 해둔다.
    count = dict(Counter(stages))

    for stage in range(1, n+1):
        # 지나간 스테이지 사람은 빼야하기 때문에 사람이 있을때만 해당 조건문을 탄다.
        # 예시에서 Stage를 넘어선 사람이 있기 때문에 stage가 count에 있는지 체크해주는 것이다.
        if people != 0 and stage in count:
            answer[stage] = count[stage] / people
            # 해당 스테이지에 있던 사람을 빼야 이후 현재스테이지사람 / 도전한사람으로 실패율이 정확해진다.
            people -= count[stage]
        else:
            answer[stage] = 0
    # answer를 정렬하는데, 키값이 아닌 value기준이기 때문에 answer[x]로 값을 기준으로 정렬해준다.
    # 실패율이 높은순이기 때문에 내림차순을 위해서 뒤집어야 한다.
    return sorted(answer, key=lambda x: answer[x], reverse=True)


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))