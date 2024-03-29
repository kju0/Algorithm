import sys
input = sys.stdin.readline

N, K = map(int, input().split())

money = []

for _ in range(N):
    tmp = int(input())

    if tmp <= K:
        money.append(tmp)

#print(money)

#큰 동전은 작은 동전의 배수이므로, 그리디 알고리즘으로 풀 수 있다.

answer = 0
while K > 0 and len(money) > 0 :
    tmp = money.pop()
    if tmp <= K:
        answer += K//tmp
        K = K - (K//tmp)*tmp

print(answer)
    
 