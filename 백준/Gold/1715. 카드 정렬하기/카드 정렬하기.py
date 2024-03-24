import heapq
import sys
input = sys.stdin.readline

N = int(input())

hq = []

for i in range(N):
    heapq.heappush(hq, int(input()))

total_cost = 0
while len(hq) > 1:
    card1 = heapq.heappop(hq)
    card2 = heapq.heappop(hq)

    sum_value = card1 + card2
    
    total_cost += sum_value

    heapq.heappush(hq, sum_value)

print(total_cost)