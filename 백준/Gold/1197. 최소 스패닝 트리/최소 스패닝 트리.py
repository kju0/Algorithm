import sys
input = sys.stdin.readline





V, E = map(int, input().split())

#서로소 집합 자료구조
parents = [i for i in range(V+1)]

def find(idx):
    if parents[idx] == idx:
        return idx
    else:
        return find(parents[idx])

def union(a, b):
    pa, pb = find(a), find(b)
    if pa == pb:
        return False
    
    if pa > pb:
        parents[pb] = pa
    else:
        parents[pa] = find(pb)
    return True

# MST 최소 신장 트리
maps = [[] for i in range(E+1)]
for i in range(1, E+1):
    a, b, cost = map(int, input().split())
    maps[i] = [cost, a, b]

# cost 순으로 정렬
maps.sort()

# 최소 간선 고르고
cnt, answer = 0, 0

for i in range(1, E+1):
    if cnt == V-1:
        break
    
    cost, a, b = maps[i][0], maps[i][1], maps[i][2]
    if union(a, b):
        cnt += 1
        answer += cost


print(answer)

