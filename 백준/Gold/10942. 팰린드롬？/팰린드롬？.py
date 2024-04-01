import sys
input = sys.stdin.readline


N = int(input())
numlist = list(input().split())
M = int(input())
dp = [[0]*(N) for _ in range(N)]

#print(dp)

#i는 팰린드롬 시작점 j는 팰린드롬 끝점
#1. 길이 1인 팰린드롬 처리
for i in range(N):
    dp[i][i] = 1
#2. 길이 2 ~ 3 인 팰린드롬 처리
for i in range(N-1):
    if numlist[i] == numlist[i+1]:
        dp[i][i+1] = 1
#3. 길이 4 이상인 팰린드롬 처리
for cnt in range(2, N):
    for i in range(N-cnt):
        end = i + cnt
        if numlist[i] == numlist[end] and dp[i+1][end-1]:
            dp[i][end] = 1

#print(dp)







for _ in range(M):
    s, e = map(int, input().split())
    if dp[s-1][e-1]:
        print(1)
    else:
        print(0)

    