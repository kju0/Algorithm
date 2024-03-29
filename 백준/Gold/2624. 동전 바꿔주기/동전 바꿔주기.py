import sys
input = sys.stdin.readline

T = int(input())
dp = [0]*(T+1)
dp[0] = 1

k = int(input())

coins = []
for i in range(k):
    p, n = map(int, input().split())

    coins.append((p, n))

coins.sort(reverse=True) 

for p, n in coins:
    for t in range(T, -1, -1):
        j = 1
        while j <= n and t - p * j >= 0:
            dp[t] += dp[t-p*j]
            j += 1
print(dp[T])
            