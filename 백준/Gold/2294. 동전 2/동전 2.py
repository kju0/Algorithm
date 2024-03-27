import sys
input = sys.stdin.readline

N, k = map(int, input().split())

coin = [0]*(101)
dp = [int(1e9)]*(10001)
dp[0] = 0
for i in range(N):
    coin[i] = int(input())

    for j in range(coin[i], k+1):
        dp[j] = min(dp[j], dp[j-coin[i]]+1)

if dp[k] == int(1e9):
    print(-1)
else:
    print(dp[k])
        



