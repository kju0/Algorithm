from collections import deque
import sys
input = sys.stdin.readline


M, N, H = map(int, input().split())

#3차원 리스트
#토마토[높이][가로][세로]
tomatoes = [[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[False]*M for _ in range(N)] for _ in range(H)]


moves = [[1, 0, 0], [-1, 0, 0], [0, -1, 0], [0, 1, 0], [0, 0, 1], [0, 0, -1]]

def searchTomato():
    dq = deque()

    tcnt = 0
    for h in range(H):
        for x in range(N):
            for y in range(M):
                if tomatoes[h][x][y] == 1:
                    dq.append((h, x, y, 0))
                elif tomatoes[h][x][y] == 0:
                    tcnt += 1
    #print(tcnt, dq)

    if tcnt == 0:
        return 0

    #토마토 체크해주기
    while dq:
        h, x, y, day = dq.popleft()
        visited[h][x][y] == True

        for i in range(6):
            nh = h + moves[i][0]
            nx = x + moves[i][1]
            ny = y + moves[i][2]

            if 0 <= nh < H and 0 <= nx < N and 0 <= ny < M and visited[nh][nx][ny] == False:
                if tomatoes[nh][nx][ny] == 0:
                    tomatoes[nh][nx][ny] = 1
                    dq.append((nh, nx, ny, day+1))
    tcnt = 0               
    for h in range(H):
        for x in range(N):
            for y in range(M):
                if tomatoes[h][x][y] == 0:
                    tcnt += 1
    
    if tcnt == 0:
        return day
    else:
        return -1


print(searchTomato())