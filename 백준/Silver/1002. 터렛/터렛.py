import math

T = int(input())


for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    # 두 원 중심 사이의 거리 구하기
    dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)

    if dist == 0 and r1 == r2:
        print(-1)
    elif dist == abs(r1 - r2) or dist == r1 + r2:
        print(1)
    elif abs(r1-r2) < dist < r1 + r2:
        print(2)
    else:
        print(0)
    