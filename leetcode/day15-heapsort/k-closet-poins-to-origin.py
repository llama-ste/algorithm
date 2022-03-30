# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).
# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

from collections import deque


class Solution:
    def k_closest(self, points, k):
        res = deque([])
        for elem in points:
            # 각요소를 제곱하여 거리값을 구하고 배열로 거리값, 원래좌표를 넣어줬다.
            # 파이썬이기 때문에 루트를 굳이 씌워주지 않았다.
            res.append([[elem[0] ** 2 + elem[1] ** 2], elem])

        sorting = deque(sorted(res))

        answer = []
        for _ in range(k):
            answer.append(sorting.popleft()[1])

        return answer


# heapq를 이용하여 푼 방법이다.
# import heapq
#
# def cal_dist(point):
#     return math.sqrt(point[0] * point[0] + point[1] * point[1])

# def k_closest_builtin(points, k):
#     dists = []
#     heap = []
#     for point in points:
#         dist = cal_dist(point)
#         heapq.heappush(heap, dist)
#         dists.append(dist)
#
#     kth_dist = [heapq.heappop(heap) for _ in range(k)][-1]
#     return [points[idx] for idx, dist in enumerate(dists) if dist <= kth_dist]