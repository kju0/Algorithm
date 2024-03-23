import sys
input = sys.stdin.readline


N, M = map(int, input().split())

parents = [i for i in range(N+1)]

def find(idx):
    if parents[idx] == idx:
        return idx
    return find(parents[idx])

def union(a, b):
    pa, pb = find(a), find(b)

    if pa == pb: #서로 연결되어 있음
        return True
    
    if pa > pb:
        parents[pa] = pb
    else:
        parents[pb] = pa
    return False

answer = N
#간선 받아주기
for i in range(M):
    u, v = map(int, input().split())

    if not union(u, v):
        answer -= 1

print(answer)