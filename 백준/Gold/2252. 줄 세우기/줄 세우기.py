from collections import deque
import sys
input = sys.stdin.readline


N, M = map(int, input().split())

#진입차수 
indegree = [0] * (N+1)
students = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    
    indegree[b] += 1
    students[a].append(b)

#print(indegree)
#print(students)

#진입차수가 0인 인덱스부터 큐에 넣어주기
dq = deque()
for i in range(1, N+1):
    if indegree[i] == 0:
        dq.append(i)
        indegree[i] -= 1

while dq:
    now = dq.popleft()

    for i in students[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            dq.append(i)
    print(now, end=" ")
            