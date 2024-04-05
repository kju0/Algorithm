
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

        #가장 먼저 등장한 위치를 알기 위해
        #lower bound 사용
        #그냥 이분탐색으로는 [-1, 1, 3, 3, 3, 4, 5, 6, 6] 이 인풋에서 오류남
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