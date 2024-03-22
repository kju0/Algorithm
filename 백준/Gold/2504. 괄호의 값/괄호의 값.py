import sys
input = sys.stdin.readline

input_str = list(input().rstrip())

stack = []

answer = 0
cost = 1
for i in range(len(input_str)):
    if input_str[i] == "(" or input_str[i] == "[":
        if input_str[i] == "(": cost *= 2
        else: cost *= 3
        stack.append(input_str[i])
    else:
        if input_str[i] == ')':
            if len(stack) == 0 or stack[-1] != '(':
                answer = 0
                break
            if input_str[i-1] == "(":
                answer += cost
                cost //= 2
                stack.pop()
            else:
                cost //= 2
                stack.pop()
        elif input_str[i] == ']':
            if len(stack) == 0 or stack[-1] != '[':
                answer = 0
                break
            if input_str[i-1] == "[":
                answer += cost
                cost //= 3
                stack.pop()
            else:
                cost //= 3
                stack.pop()

if len(stack) != 0:
    answer = 0
        
print(int(answer))

    