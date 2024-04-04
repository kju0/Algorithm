import sys
input = sys.stdin.readline
import heapq


N, K = list(map(int,input().split()))
jewelys = []
bags = []
heap=[]

answer=0

for i in range(N):
    jewelys.append(list(map(int,input().split())))
for i in range(K):
    bags.append(int(input().rstrip()))

jewelys.sort(key = lambda x: x[0])
bags.sort()
i=0
for bag in bags:
    while i < N and bag >= jewelys[i][0]:
        heapq.heappush(heap,-jewelys[i][1])
        i=i+1
    if heap != []:
        answer = answer + heapq.heappop(heap)
print(-answer)