import sys
input = sys.stdin.readline

N = int(input())

stack = []
for _ in range(N):
    stack.append(int(input()))

#마지막은 무조건 보이니까 answer = 1
answer = 1
max_val = stack[-1]
for i in range(N-1, -1, -1):
    if max_val < stack[i]:
        answer += 1
        max_val = stack[i]

print(answer)