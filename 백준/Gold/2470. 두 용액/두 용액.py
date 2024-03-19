import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

arr.sort()

start, end = 0, N-1 #arr index

ansList = [0, 0]
answer = sys.maxsize
while start < end:
    
    if abs(arr[start] + arr[end]) < answer:
        answer = abs(arr[start]+arr[end])
        ansList[0] = arr[start]
        ansList[1] = arr[end]
    
        if answer == 0:
            break    
    else:
        if abs(arr[start]) < abs(arr[end]):
            end -= 1
        else:
            start += 1

print(ansList[0], ansList[1])