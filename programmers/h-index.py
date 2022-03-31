def solution(citations):
    citations.sort(reverse=True)

    print(citations)

    # H-index는 특정 연구원의 연구 성과를 평가하기 위한 지표
    # 나의 h는 어떻게 구할 수 있을까? 자신이 저널에 등재한 전체 논문중 많이 인용된 순으로 정렬한 후,
    # 피인용수가 논문수와 같아지거나 피인용수가 논문수보다 작아지기 시작하는 숫자가 바로 나의 h가 됩니다.

    # index가 0부터 시작하기 떄문에 통과를 못했을때의 인덱스를 반환하면 정확한 수가 나오게 되는것이다.
    # 모두 통과 하였을경우에는 전체가 h번이상 인용되었기 때문에 length를 반환하면 전체 논문수가 된다.
    for i, v in enumerate(citations):
        # 피인용수로 정렬하였기 때문에 index가 피인용수랑 같거나 작아진다면 이후에도 작아지기 때문에 반복문을 끝낸다.
        if i >= v:
            return i
    return len(citations)