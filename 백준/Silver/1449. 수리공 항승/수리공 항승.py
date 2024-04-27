N, L = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

answer = 1
target = arr[0]

for i in range(1, N):

    if arr[i] < target+L:
        continue

    else:
        target = arr[i]
        answer += 1

print(answer)