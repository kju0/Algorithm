#dummy
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
K = int(input())

#맵 그리기
maps = [[0]*N for _ in range(N)]

#사과 받기 사과 좌표는 2
for i in range(K):
    x, y = map(int, input().split())
    maps[x-1][y-1] = 2

#print(maps)
L = int(input())

moves = [[0]*L, ['']*L]
for i in range(L):
    time, move = input().split()
    moves[0][i] = int(time)
    moves[1][i] = move

#좌 상 우 하
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

#이동 변환 함수
def change(now, move):
    if move == "D": #오른쪽
        now += 1
        if now > 3: now = 0
    else: #왼쪽
        now -= 1
        if now < 0: now = 3
    return now


time, idx = 0, 2
snake = deque([])
snake.append([0,0]) #snake[0] 사과 없으면 사라질 꼬리, snake[-1] 늘려줄 머리

while True:
    #print(f'{time}초 snake 큐 {snake} 방향은 {idx}')
    time += 1
    x, y = snake[-1]
    #뱀 머리 늘리기
    nx, ny = x+dx[idx], y+dy[idx]
    
    #늘린 머리가 종료 조건인지 확인
    if 0 > nx or N <= nx or 0 > ny or N <= ny or [nx, ny] in snake:
        break

    #일단 넣기
    snake.append([nx, ny])
    #늘린 머리 좌표에 사과가 있는지 확인
    if maps[nx][ny] != 2:
        #사과 있으면 사과 지우기
        snake.popleft()
    else:
        maps[nx][ny] = 0
    
    #모든 작업이 끝난 후 방향 바꿔주기
    if time in moves[0]:
        idx = change(idx, moves[1][moves[0].index(time)])

print(time)
        
    
