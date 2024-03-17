import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


n = int(input())
nlist = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_ans = -(1e9)
min_ans = 1e9

def solve(depth, total):
    global add, sub, mul, div, max_ans, min_ans

    if depth == n:
        max_ans = max(max_ans, total)
        min_ans = min(min_ans, total)
        return
    
    if add > 0:
        add -= 1
        solve(depth+1, total+nlist[depth])
        add += 1
    if sub > 0:
        sub -= 1
        solve(depth+1, total-nlist[depth])
        sub += 1
    if mul > 0:
        mul -= 1
        solve(depth+1, total*nlist[depth])
        mul += 1
    if div > 0:
        div -= 1
        solve(depth+1, int(total/nlist[depth]))
        div += 1

solve(1, nlist[0])

print( int(max_ans), int(min_ans), sep="\n")