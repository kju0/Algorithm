from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
map = [list(map(int, input().rstrip())) for _ in range(N)]

#상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[-1]*N for _ in range(N)]

dq = deque([(0,0)])
visited[0][0] = 0

while dq:
    #dq에서 빼면서 해당 위치가 검은색인지 흰색인지 확인
    x, y = dq.popleft()

    if x == N-1 and y == N-1:
        print(visited[N-1][N-1])
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx  < N and 0 <= ny < N and visited[nx][ny] == -1:
            if map[nx][ny] == 1:
                visited[nx][ny] = visited[x][y]
                dq.appendleft((nx, ny))
            elif map[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                dq.append((nx, ny))

