import sys
input = sys.stdin.readline


T = int(input())
arr = []
for _ in range(T):
    arr.append(int(input().rstrip()))

arr.sort()

for i in range(T):
    print(arr[i])