import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


#방문 여부 확인 visit 리스트 필요
#재귀 종료 조건 필요
#종료 시 cost 계속 비교
def solve(start, now, val, depth):
    global answer
    if depth == n:
        if arr[now][start]:
            if answer > val + arr[now][start]:
                answer = val + arr[now][start]
        return
    
    for i in range(n):
        if not visit[i] and arr[now][i] != 0:
            visit[i] = True
            solve(start, i, val+arr[now][i], depth+1)
            visit[i] = False

n = int(input())
arr = [[0 for _ in range(n)] for _ in range(n)]
visit = [0]*n

for i in range(n):
    arr[i] = list(map(int, input().split()))


answer = sys.maxsize

for i in range(n):
    #n개 좌표들 시작점으로 하기
    visit[i] = True
    solve(i, i, 0, 1)
    visit[i] = False

print(answer)







