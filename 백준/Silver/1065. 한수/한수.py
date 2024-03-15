def boj_input():
    n = int(input())
    return n

def solution():
    n = boj_input()
    if n < 100:
        answer = n
    else:
        answer = 99
    for i in range(100, n+1):
        a, b, c = int(str(i)[0]), int(str(i)[1]), int(str(i)[2])
        if (a-b) == (b-c):
            answer += 1
    
    print(answer)

solution()