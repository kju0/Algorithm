import sys
input = sys.stdin.readline

N = int(input())

stack = []

for _ in range(N):
    a, b = map(int, input().split())
    if a <= b:
        if len(stack) == 0:
            stack.append(b)
        elif stack[-1] > b:
            stack.pop()
            stack.append(b)

if len(stack) == 0:
    print(-1)
else:
    print(stack[-1])
    
    
    