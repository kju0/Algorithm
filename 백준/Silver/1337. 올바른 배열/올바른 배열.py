import sys
input = sys.stdin.readline

n = int(input())

arr = [0 for _ in range(n)]
for i in range(n):
    arr[i] = int(input())

arr.sort()

answer = 0
start = 0
for i in range(n):
    start = i
    end = arr[i] + 4
    tmp = 0 
    while (start != n):
        if arr[start] <= end:
            tmp += 1
        start += 1
    answer = max(answer, tmp)
#print(arr)
print(5-answer)