import sys
input = sys.stdin.readline

K, N = map(int, input().split())

arr = [0]*K

for i in range(K):
    arr[i] = int(input())

arr.sort()

start, end = 1, arr[-1]
answer = 0

while start <= end:
    mid = (start+end)//2

    total = 0
    for i in range(K):
        total += (arr[i]//mid)
    
    if total < N:
        end = mid - 1
    else:
        start = mid+1
        answer = max(answer, mid)

print(answer)