import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):

    N = int(input())

    score = [list(map(int, input().split())) for _ in range(N)]

    score.sort()
    answer = 1
    max_ = score[0][1]
    for i in range(1, N):

        if max_ > score[i][1]:
            answer += 1
            max_ = score[i][1]

    print(answer)