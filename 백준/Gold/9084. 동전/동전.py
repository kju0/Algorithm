import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())

    coins = list(map(int, input().split()))
    M = int(input())

    dp = [0]*(M+1)
    dp[0] = 1

    # m은 M부터 1까지
    # coins[i]

    for i in range(len(coins)-1, -1, -1):
        coin = coins[i]
        for m in range(M, -1, -1):
            j = 1
            while m - j * coin >= 0 and j <= m:
                dp[m] += dp[m - j * coin]
                j += 1

    print(dp[M])