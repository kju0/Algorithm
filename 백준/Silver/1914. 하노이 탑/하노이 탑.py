import sys
sys.setrecursionlimit(10**6)

def hanoi(idx, start, target, ass):
    if idx == 1:
        print(start, target, sep=" ")
        return
    hanoi(idx-1, start, ass, target) #경유지로 보내주기
    print(start, target, sep=" ")
    hanoi(idx-1, ass, target, start)
        

n = int(input())
print(2**n-1)
if n <= 20:
    hanoi(n, 1, 3, 2)