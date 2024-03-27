from collections import deque
import sys
input = sys.stdin.readline

#박스 최대 맥주는 20개까지
#50m마다 맥주 먹어줘야 함 = 1000m까지만,
T = int(input())

for _ in range(T):
    n = int(input())

    start = list(map(int, input().split()))
    conv = [list(map(int, input().split())) for _ in range(n)]
    conv.sort()

    end = list(map(int, input().split()))

    conv = conv + [end]
    #print(start)
    #print(end)
    #print(conv)


    dq = deque()
    dq.append((start[0], start[1]))

    visited = [False]*(n+1)
    ans = False
    while dq:
        #현재 위치


        x, y = dq.popleft()

        if x == end[0] and y== end[1]:
            ans = True
            break

        #1000m 이내로 갈 수 있는 모든 편의점 dq에 넣어주기
        for i in range(n+1):
            convX, convY = conv[i][0], conv[i][1]

            if abs(convX - x) + abs(convY - y) <= 1000 and not visited[i]:
                visited[i] = True
                dq.append(conv[i])

    if not ans:
        print("sad")
    else:
        print("happy")




    

