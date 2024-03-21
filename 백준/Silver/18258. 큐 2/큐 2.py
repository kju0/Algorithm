import sys
input = sys.stdin.readline

N = int(input())

q = []
first = 0

for _ in range(N):
    input_str = list(map(str, input().split()))
    
    if input_str[0] == "push":
        q.append(input_str[1])
    elif input_str[0] == "pop":
        if len(q) > first:
            print(q[first])
            first += 1
        else:
            print(-1)
    elif input_str[0] == "size":
        print(len(q)-first)
    elif input_str[0] == "empty":
        if len(q) == first:
            print(1)
            q = []
            first = 0
        else:
            print(0)
    elif input_str[0] == "front":
        if len(q) <= first:
            print(-1)
        else:
            print(q[first])
    elif input_str[0] == "back":
        if len(q) <= first:
            print(-1)
        else:
            print(q[-1])