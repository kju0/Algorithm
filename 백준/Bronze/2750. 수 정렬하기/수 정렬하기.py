T = int(input())

arr = []
for _ in range(T):
    arr.append(int(input()))

arr.sort()

for i in range(T):
    print(arr[i])