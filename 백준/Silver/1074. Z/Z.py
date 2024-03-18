import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
n, r, c = map(int, input().split())

#분할 정복으로 풀어보기!


base = [0,0]
cost = 0
now = 0
#1.일단 가장 처음 몇 사분면인지 맞추는 함수 만들기
#각 사분면 당 해당하는 좌표는 기본적으로 n값에 따라 달라진다.
def z(n, base):
    global cost
    #print(n, base)

    if n >= 1:
        if base[0] <= r < base[0]+2**(n-1) and base[1] <= c < base[1]+2**(n-1):
            #print(f'현재 {n}일 때 사분면은 1')
            now = 1
            base = [base[0], base[1]]
        elif base[0] <= r < base[0]+2**(n-1) and base[1]+2**(n-1) <= c < base[1]+2*2**(n-1):
            #print(f'현재 {n}일 때 사분면은 2')
            now = 2
            base = [base[0], base[1]+2**(n-1)]
        elif base[0]+2**(n-1) <= r < base[0]+2*2**(n-1) and base[1] <= c < base[1]+2**(n-1):
            #print(f'현재 {n}일 때 사분면은 3')
            now = 3
            base = [base[0]+2**(n-1), base[1]]
        else:
            #print(f'현재 {n}일 때 사분면은 4')
            now = 4
            base = [base[0]+2**(n-1), base[1]+2**(n-1)]
        
        cost += 4**(n-1)*(now-1)
        z(n-1, base)


z(n, base)
print(cost)
#재귀로 풀어보기!