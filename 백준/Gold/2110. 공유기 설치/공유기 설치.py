import sys
input = sys.stdin.readline

N, C = map(int, input().split())

#가장 인접한 두 공유기의 거리가 최대로!
arr = [0]*N
for i in range(N):
    arr[i] = int(input())

max_dist = 0

#일단 정렬
arr.sort()

start, end = 1, arr[-1]-arr[0]

while start <= end:
    mid = (start+end)//2
    
    cnt = 1
    current = arr[0]
    for i in range(1, N):
        if arr[i] >= current + mid:
            cnt += 1
            current = arr[i]

    
    #print(start, end, mid, cnt)
    if cnt < C:
        end = mid-1
    else:
        start = mid+1
        max_dist = max(mid, max_dist)

print(max_dist)