import sys
input = sys.stdin.readline

arr1 = input().rstrip()
arr2 = input().rstrip()


arr = [[0]* (len(arr1)+1) for _ in range(len(arr2)+1)]


for i in range(len(arr2)):
    for j in range(len(arr1)):
        if arr2[i] == arr1[j]:
            arr[i+1][j+1] = arr[i][j] + 1
        else:
            arr[i+1][j+1] = max(arr[i+1][j], arr[i][j+1])

print(arr[len(arr2)][len(arr1)])
