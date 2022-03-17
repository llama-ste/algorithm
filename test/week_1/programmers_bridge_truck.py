bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]


def solution(bridge_len, total_weight, truck_weight):
    answer = 0
    # truck의 길이만큼 빈리스트를 만들어준다.
    truck_on_bridge = [0] * bridge_len

    # 다리의 길이가 남아있는 동안 반복문을 돈다.
    while len(truck_on_bridge) > 0:
        #시작하면 바로 다리를 건너기 시작하기 때문에 answer를 1씩 더해준다.
        answer += 1
        # 트럭이나 다시 0이 추가될것이기 때문에 queue처럼 맨앞에 있는것을 빼준다.
        truck_on_bridge.pop(0)

        # 트럭이 남아있는 동안 계속 반복된다.
        if truck_weight:
            # 다리위의 트럭 + 0번트럭 무게를 다리가 버틸수 있는지 확인한다.
            if sum(truck_on_bridge) + truck_weight[0] <= total_weight:
                # 버틸 수 있다면 다음 트럭을 다리위에 넣어준다.
                truck_on_bridge.append(truck_weight.pop(0))
            else:
                # 버틸 수 없다면 다리길이를 유지해야 되기 때문에 0을 추가해준다.
                truck_on_bridge.append(0)

    return answer


print(solution(bridge_length, weight, truck_weights))