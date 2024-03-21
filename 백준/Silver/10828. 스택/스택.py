import sys
input = sys.stdin.readline


stack = []

N = int(input())

#입력 처리
for i in range(N):
    input_str = list(map(str, input().split()))
    
    if input_str[0] == "push":
        stack.append(input_str[1])
    if input_str[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            tmp = stack.pop()
            print(tmp)
    if input_str[0] == "size":
        print(len(stack))
    if input_str[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    if input_str[0] == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])