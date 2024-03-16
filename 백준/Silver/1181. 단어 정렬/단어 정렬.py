import sys
input = sys.stdin.readline

N = int(input())

strList = [set() for i in range(51)]

for _ in range(N):
    now = input().rstrip()
    strList[len(now)].add(now)

for i in range(51):
    if len(strList[i]) != 0:
        strList[i] = sorted(strList[i])
        for j in strList[i]:
            print(j)