import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
arr = [[] for _ in range(n)]
for i in range(n):
    arr[i] = list(map(int, input().split()))


#print(arr)

white, blue = 0, 0

def solve(x, y, depth):
    global blue
    global white
    #파란색 1 검사하기
    tmp_blue = 0
    for i in range(x, x+depth):
        for j in range(y, y+depth):
            if arr[i][j]:
                tmp_blue += 1
    
    #모두 파란색이 아닌 경우 
    if not tmp_blue: white+=1
    elif tmp_blue == depth*depth: blue+=1
    else:
        solve(x, y, depth//2)
        solve(x, y+depth//2, depth//2)
        solve(x+depth//2, y, depth//2)
        solve(x+depth//2, y+depth//2, depth//2)
    
    return

solve(0, 0, n)
print(white)
print(blue)