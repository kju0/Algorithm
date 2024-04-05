
import sys
input = sys.stdin.readline


N, M = map(int, input().split())

arr = [int(input()) for _ in range(N)]

#이진탐색을 위해 sort
arr.sort()

def find(num):
    result = -1
    start, end = 0, N-1

    while start <= end:
        mid = (start+end)//2
        
        if arr[mid] < num:
            start = mid + 1
        elif arr[mid] > num:
            end = mid - 1
        elif arr[mid] == num:
            if end == mid:
                break
            end = mid
    
    if arr[mid] == num:
        return mid
    else:
        return result

for _ in range(M):
    tmp = int(input())
    idx = find(tmp)
    print(idx)
    








