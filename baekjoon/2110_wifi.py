def install_router(lst, C):
    # 1. 이분탐색을 위한 정렬
    lst.sort()

    # 2. 이분탐색 대상은 '최대거리'.
    # 최솟값은 1, 최댓값은 양 끝값의 차이.
    lo = 1
    hi = lst[-1] - lst[0]
    min_gap = 0

    # 3. 최대 거리를 찾을 때까지 이분탐색
    while lo <= hi:
        # 중간 거리를 시험해본다.
        mid = (lo + hi) // 2

        # 0번째 요소에 항상 설치하므로 1개를 깔고 간다.
        cnt = 1
        # 0번째 요소부터 시작.
        cur = lst[0]

        # 1번째 ~ 마지막 요소를 연결시켜본다.
        for i in range(1, len(lst)):
            # 연결만 된다면 더 멀리 있는 것도 괜찮다
            # 이해가 안된다면 문제의 예시인
            # [1, 2, 4, 8, 9] 를 최대거리 3으로 연결하는 경우를 찬찬히 생각해보자.
            # (1, 4, 8)에 설치한 경우, 1~4 거리는 3, 4~8 거리는 4다.
            # 가장 인접한 두 점의 최대 거리가 3이므로 4가 괜찮은 것이다.
            if lst[i] >= cur + mid:
                cur = lst[i]
                cnt += 1

        if cnt >= C:
            min_gap = mid
            lo = mid + 1
        else:
            hi = mid - 1

    def install_router(lst, C):
        # 1. 이분탐색을 위한 정렬
        lst.sort()

        # 2. 이분탐색 대상은 '최대거리'.
        # 최솟값은 1, 최댓값은 양 끝값의 차이.
        lo = 1
        hi = lst[-1] - lst[0]
        min_gap = 0

        # 3. 최대 거리를 찾을 때까지 이분탐색
        while lo <= hi:
            # 중간 거리를 시험해본다.
            mid = (lo + hi) // 2

            # 0번째 요소에 항상 설치하므로 1개를 깔고 간다.
            cnt = 1
            # 0번째 요소부터 시작.
            cur = lst[0]

            # 1번째 ~ 마지막 요소를 연결시켜본다.
            for i in range(1, len(lst)):
                # 연결만 된다면 더 멀리 있는 것도 괜찮다
                # 이해가 안된다면 문제의 예시인
                # [1, 2, 4, 8, 9] 를 최대거리 3으로 연결하는 경우를 찬찬히 생각해보자.
                # (1, 4, 8)에 설치한 경우, 1~4 거리는 3, 4~8 거리는 4다.
                # 가장 인접한 두 점의 최대 거리가 3이므로 4가 괜찮은 것이다.
                if lst[i] >= cur + mid:
                    cur = lst[i]
                    cnt += 1

            if cnt >= C:
                min_gap = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return min_gap

    assert install_router([1, 2, 8, 4, 9], 3) == 3
    return min_gap


assert install_router([1, 2, 8, 4, 9], 3) == 3