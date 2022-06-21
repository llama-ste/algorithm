nums = int(input())

for _ in range(nums):
    brackets = input()
    stack = []

    for char in brackets:
        if char == "(":
            stack.append(char)
        else:
            if stack:
                stack.pop()
            else:
                stack.append(char)
                break

    print("NO" if stack else "YES")

