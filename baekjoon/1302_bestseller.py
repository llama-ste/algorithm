from collections import Counter

# 1번 풀이 방법
books = [input() for _ in range(int(input()))]

best = Counter(books).most_common()

candidate = []

for key, value in best:
    most = best[0][1]
    if most == value:
        candidate.append(key)

print(sorted(candidate)[0])


# 2번 풀이 방법
# d = dict()
#
# for _ in range(int(input())):
#     book = input()
#     if book in d:
#         d[book] += 1
#     else:
#         d[book] = 1
#
# best = max(d.values())
#
# candidate = []
#
# for k, v in d.items():
#     if v == best:
#         candidate.append(k)
#
# print(sorted(candidate)[0])