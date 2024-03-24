import sys
from collections import deque
input = sys.stdin.readline

N, M, K, X = map(int, input().split())

roads = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int,input().split())

    roads[a].append(b)

#print(roads)

answer = [int(1e9)]*(N+1)
#X에서 출발했을 때 최단거리가 K인 모든 도시를 구해라!
#하나도 없는 경우 -1

dq = deque()
dq.append(X)

answer[X] = 0

while dq:
    idx = dq.popleft()

    for i in roads[idx]:
        if answer[i] > answer[idx]+1:
            answer[i] = answer[idx]+1
            dq.append(i)

if answer.count(K) == 0:
    print(-1)
else:
    for i in range(1, N+1):
        if answer[i] == K:
            print(i)