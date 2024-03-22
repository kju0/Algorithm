import sys
input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))

def find(stack, val):
    while stack:
        if arr[stack[-1]-1] >= val:
            return stack[-1]
        else:
            stack.pop()
    return 0

stack= [1]
print(0, end=" ")


for i in range(1, N):
    #1. 현재 arr[i]보다 큰 값 스택에서 찾기
    if i != N-1:
        print(find(stack, arr[i]), end=" ")
    else:
        print(find(stack, arr[i]))
    stack.append(i+1)