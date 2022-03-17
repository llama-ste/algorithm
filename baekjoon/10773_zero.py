leng = 10
stack = []

for i in range(leng):
    num = 0 if i % 2 == 0 else 3

    # stack이 안비어있거나, 0이 들어온다면 바로 앞의 데이터를 빼야한다.
    if len(stack) > 0 and num == 0:
        stack.pop()
    else:
        #아니라면 들어온 숫자를 스택에 쌓아준다.
        stack.append(num)

print(sum(stack))