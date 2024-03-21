from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

kidx = 0
dq = deque(i for i in range(1, N+1))
kidx = 0
anslist = []
print("<", end="")
while dq:
    tmp = dq.popleft()
    kidx += 1

    if kidx == K:
        kidx = 0
        if dq:
            print(tmp, end=", ")
        else:
            print(tmp, end=">")
    else:    
        dq.append(tmp)
        
