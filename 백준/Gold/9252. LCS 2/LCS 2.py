import sys
input = sys.stdin.readline

arr1 = [0] + list(input().rstrip())
arr2 = [0] + list(input().rstrip())

arr = [['']*(len(arr1)) for _ in range(len(arr2))]

for i in range(1, len(arr2)):
    for j in range(1, len(arr1)):
        if arr2[i] == arr1[j]:
            arr[i][j] = arr[i-1][j-1] + arr1[j]
        else:
            if len(arr[i][j-1]) > len(arr[i-1][j]):
                arr[i][j] = arr[i][j-1]
            else:
                arr[i][j] = arr[i-1][j]

print(len(arr[-1][-1]))
if len(arr[-1][-1]) != 0:
    print(arr[-1][-1])