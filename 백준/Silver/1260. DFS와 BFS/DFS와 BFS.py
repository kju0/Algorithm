from collections import deque
import sys
sys.setrecursionlimit(10**5)

input = sys.stdin.readline


N, M, V = map(int, input().split())

arr = [[] for _ in range(N+1)]

for i in range(M):
    v1, v2 = map(int, input().split())
    arr[v1].append(v2)
    arr[v2].append(v1)

#print(arr)

for i in range(N+1):
    arr[i].sort()

visited = [False] * (N+1)

def dfs(idx):
    visited[idx] = True
    print(idx, end=" ")
    for i in arr[idx]:
        if visited[i] == False:
            dfs(i)


def bfs(idx):
    dq = deque()
    dq.append(idx)
    visited[idx] = True

    while dq:
        tmp = dq.popleft()
        print(tmp, end=" ")
        for i in arr[tmp]:
            if visited[i] == False:
                dq.append(i)
                visited[i] = True
    
dfs(V)
print()
visited = [False] * (N+1)
bfs(V)