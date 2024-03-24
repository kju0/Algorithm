import sys
from collections import deque
input = sys.stdin.readline

K = int(input())


def dfs(idx):
    stack.append((idx, color[idx]))

    while stack:
        v, c = stack.pop()

        for i in arr[v]:
            if color[i] == -1:
                color[i] = not(c)
                stack.append((i, color[i]))
            else:
                if color[i] == c:
                    return False


    return True


for _ in range(K):
    V, E = map(int, input().split())
    arr = [[] for _ in range(V+1)]
    color = [-1]*(V+1)
    answer = True
    for _ in range(E):
        u, v = map(int, input().split())

        arr[u].append(v)
        arr[v].append(u)
    
    #헷갈리는 관계로 stack으로 해결해보자!
    stack = deque()
    for i in range(1, V+1):
        if color[i] == -1:
            color[i] = not(color[i])
            if not dfs(i):
                answer = False
                break
    
    if answer:
        print("YES")
    else:
        print("NO")