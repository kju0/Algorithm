import sys
input = sys.stdin.readline


N, K = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

#print(arr)


dp = [[0]*(K+1) for _ in range(N+1)]

#print(dp)

for i in range(1, N+1):
    weight, value = arr[i-1][0], arr[i-1][1]

    for j in range(1, K+1):
        if j < weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-weight]+value, dp[i-1][j])

print(dp[-1][-1])