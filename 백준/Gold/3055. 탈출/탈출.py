from collections import deque
import sys
input = sys.stdin.readline


r, c = map(int, input().split())
map = [list(input().rstrip()) for _ in range(r)]

visited = [[-1]*c for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
dq = deque()

#위치 파악
for i in range(r):
    for j in range(c):
        if map[i][j] == "*":
            dq.appendleft((i,j))
        elif map[i][j] == "S":
            dq.append((i, j))
            visited[i][j] = 0

def solve():
    while dq:
        x, y = dq.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 > nx or nx >= r or 0 > ny or ny >= c or visited[nx][ny] != -1:
                continue

            if map[nx][ny] == "X" or map[nx][ny] == "*": #돌맹이거나 물이면 탐색 x
                continue

            if map[x][y] == "*" and map[nx][ny] == "D":
                continue

            if map[x][y] == "S":
                if map[nx][ny] == "D":
                    return visited[x][y] + 1
                else:
                    visited[nx][ny] = visited[x][y] + 1
            
            map[nx][ny] = map[x][y]
            dq.append((nx, ny))
    
    return "KAKTUS"

            



print(solve())
        

    



