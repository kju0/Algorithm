from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

# 입력처리
# 1. 상위 제품 - 필요 제품 개수 연결 정보를 담을 arr
# 2. 진입차수 indegree
# 3. 진입차수가 0인 것들만 가지는 basic_parts
arr = [[] for _ in range(N+1)]
indegree = [0]*(N+1)

for _ in range(M):
    x, y, k = map(int, input().split())

    #하위 부품에 상위 부품 정보를 넣어준다!
    arr[y].append([x, k])
    indegree[x] += 1

basic_parts = []
for i in range(1, N+1):
    if indegree[i] == 0:
        basic_parts.append(i)

# 완제품,중간부품,기본부품 별로 필요로 하는 기본 부품 정보 저장해주기!
#일단 0으로 초기화
needList = [{j: 0 for j in basic_parts} for _ in range(N+1)]

#기본 부품들은 필요로 하는 기본 부품이 없으므로 자기 자신은 1로 넣어주기!
for idx in basic_parts:
    needList[idx][idx] = 1

dq = deque(basic_parts)
while dq:
    now = dq.popleft()

    for x, k in arr[now]: #now를 필요로 하는 상위 제품과 now 개수
        for idx in needList[x].keys():
            needList[x][idx] += needList[now][idx] * k
        
        indegree[x] -= 1
        if indegree[x] == 0:
            dq.append(x)

for key, value in needList[N].items():
    print(f'{key} {value}')