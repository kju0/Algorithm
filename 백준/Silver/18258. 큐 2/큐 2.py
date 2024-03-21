import sys
input = sys.stdin.readline

from collections import deque

N = int(input())

deq = deque()

for _ in range(N):
    input_str = list(map(str, input().split()))
    
    if input_str[0] == "push":
        deq.append(input_str[1])
    elif input_str[0] == "pop":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.popleft())
    if input_str[0] == "size":
        print(len(deq))
    if input_str[0] == "empty":
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    if input_str[0] == "front":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[0])
    if input_str[0] == "back":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[-1])