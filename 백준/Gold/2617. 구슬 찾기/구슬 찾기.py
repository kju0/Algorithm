import sys
input = sys.stdin.readline

N, M = map(int, input().split())

light_list = [[] for _ in range(N+1)]
heavy_list = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    #구슬 a보다 가벼운 구슬 b 정보를 가지는 arr
    light_list[a].append(b)
    heavy_list[b].append(a)



def dfs(idx, arr):
    visited = [False] * (N+1)
    stack = []
    stack.append(idx)
    visited[idx] = True
    cnt = 0
    while stack:
        now = stack.pop()

        for i in arr[now]:
            if not visited[i]:
                visited[i] = True
                cnt += 1
                stack.append(i)
    
    return cnt

answer = 0
for i in range(1, N+1):
    
    if dfs(i, light_list) >= (N//2+1) or dfs(i, heavy_list) >= (N//2+1):
        answer += 1

print(answer)



