# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).
# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

from collections import deque


class Solution:
    def k_closest(self, points, k):
        res = deque([])
        for elem in points:
            # 각요소를 제곱하여 거리값을 구하고 배열로 거리값, 원래좌표를 넣어줬다.
            res.append([[elem[0] * elem[0] + elem[1] * elem[1]], elem])

        sorting = deque(sorted(res))

        answer = []
        for _ in range(k):
            answer.append(sorting.popleft()[1])

        return answer
