from collections import deque
import copy
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [list(map(int,input().split())) for _ in range(N)]

#print(graph)

#상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#빙하를 하나씩 녹여줄건데, 그 다음에 어떻게 영향을 안끼치게 할까
#한 덩이인지 여러 덩이인지 확인은 어떻게 해줄까


def bfs(x, y):   
    dq.append((x, y))

    while dq:
        i, j = dq.popleft()
        visited[i][j] = True
        
        melt = 0
        
        for r in range(4):
            nx = i + dx[r]
            ny = j + dy[r]

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if graph[nx][ny] != 0:
                    visited[nx][ny] = True
                    dq.append((nx, ny))
                else:
                    melt += 1
        new_graph[i][j] -= melt
        if new_graph[i][j] < 0:
            new_graph[i][j] =0

chk = False
answer = 0

while True:
    dq = deque()
    new_graph = copy.deepcopy(graph)
    ice = 0
    visited = [[False]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if graph[i][j] > 0 and not visited[i][j]:
                bfs(i, j)
                ice += 1
    
    graph = new_graph
    if ice == 0:
        break
    if ice >= 2:
        chk = True
        break
    
    answer += 1

if chk:
    print(answer)
else:
    print(0)

    
    

