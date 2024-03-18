import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

def solve(a, b, c):
    if b == 1:
        return a%c
    if b % 2 == 0:
        return (solve(a,b//2,c)**2%c)
    else:
        return ((solve(a,b//2,c)**2)*a)%c

print(solve(a, b, c))