import sys
from collections import deque
input = sys.stdin.readline

N, M, K, X = map(int, input().split())

roads = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int,input().split())
    roads[a].append(b)

#print(roads)

dist = [0]*(N+1)
visited = [False]*(N+1)
answer = []
#X에서 출발했을 때 최단거리가 K인 모든 도시를 구해라!
#하나도 없는 경우 -1

dq = deque()
dq.append(X)

visited[X] = True
dist[X] = 0
while dq:
    idx = dq.popleft()

    for i in roads[idx]:
        if not visited[i]:
            visited[i] = True
            dq.append(i)
            dist[i] = dist[idx] + 1
            if dist[i] == K:
                answer.append(i)


if len(answer) == 0:
    print(-1)
else:
    answer.sort()
    for i in answer:
        print(i)


