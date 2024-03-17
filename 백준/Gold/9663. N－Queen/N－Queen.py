
n = int(input())

#arr[i] = j 는 i행의 j열에 체스를 놓는다는 뜻이다.
arr = [0]*n
answer = 0

def promising(row):
    for i in range(row):
        if arr[row] == arr[i] or row - i == abs(arr[row]-arr[i]):
            return False
    return True

def solve(row):
    global answer
    if row == n:
        answer += 1
        return
    
    #depth가 아직 n이 아닐 때
    #넣어줄 수 있는지 아닌지 검사해야 함
    #1. 이전에 놓은 체스들과 같은 열의 값을 가지면 안됨
    #2. 대각선이면 안됨!
    for y in range(n):
        arr[row] = y
        if promising(row):
            solve(row + 1)
    
#0행의 0, 1, ... n-1까지 다 넣어보며 테스트해야 함.
solve(0)


print(answer)