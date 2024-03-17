import sys
import itertools
input = sys.stdin.readline

def abssum(arr):
    result = 0
    for i in range(len(arr)-1):
        result += abs(arr[i]-arr[i+1])
    
    return result

N = int(input())
arr = list(map(int, input().split()))
answer = 0
perlists = itertools.permutations(arr)

for perlist in perlists:
    tmp = abssum(perlist)
    if tmp > answer:
        answer = tmp

print(answer)


