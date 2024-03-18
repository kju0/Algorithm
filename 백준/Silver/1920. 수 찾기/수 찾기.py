import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())
mlist = list(map(int, input().split()))

A.sort()

def binary_search(arr, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2

    if arr[mid] == target:
        return True
    
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid-1)
    else:
        return binary_search(arr, target, mid+1, end)

for i in range(M):
    if binary_search(A, mlist[i], 0, N-1) == None:
        print(0)
    else:
        print(1)
    
