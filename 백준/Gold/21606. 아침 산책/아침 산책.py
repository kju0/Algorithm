import sys
input = sys.stdin.readline

N = int(input())

#실내 실외 구분 string
gubun = input().rstrip()

arr = [[] for i in range(N+1)]

for i in range(N-1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)


#print(arr)

#경로 개수
answer = 0

def dfs(idx):
    global answer
    visited[idx] = True

    for i in arr[idx]:
        if visited[i] == False:
            if gubun[i-1] == "0": #실외인 경우 탐색 ing
                dfs(i)
            else:
                answer += 1

for i in range(1, N+1):
    #시작점 바뀔 때마다 초기화 -> 정녕 이 방법이 최선인고
    visited = [False]*(N+1)
    #실내 gubun[i-1] == 1인 경우 탐색 시작
    if gubun[i-1] == "1":
        dfs(i)

print(answer)
