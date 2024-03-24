import sys
import heapq
input = sys.stdin.readline

N = int(input())
M = int(input())

buslist = [[] for _ in range(N+1)]

for _ in range(M):
    bus1, bus2, cost = map(int,input().split())

    buslist[bus1].append([bus2, cost])

start, end = map(int, input().split())

dist = [int(1e9)]*(N+1)
dq = [(start, 0)]

dist[start] = 0

while dq:
    now, cost = heapq.heappop(dq)
    
    if dist[now] < cost: #종료조건 필요
        continue

    for idx, c in buslist[now]:
        if dist[idx] > dist[now] + c:
            dist[idx] = dist[now] + c
            heapq.heappush(dq, (idx, dist[now]+c))

print(dist[end])
