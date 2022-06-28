num = int(input())

def add(i):
    if i == 1:
        return 1
    elif i == 2:
        return 2
    elif i == 3:
        return 4

    return add(i-1) + add(i-2) + add(i-3)


for i in range(num):
    i = int(input())

    print(add(i))