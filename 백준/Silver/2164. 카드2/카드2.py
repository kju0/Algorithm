from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

cards = deque([i for i in range(1, N+1)])

while True:
    if len(cards) == 1:
        break
    cards.popleft()
    tmp = cards.popleft()
    cards.append(tmp)

print(cards.popleft())
