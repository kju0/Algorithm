import sys
input = sys.stdin.readline


N = int(input())

gubun = ["0"] + list(input().rstrip())

arr = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())

    arr[a].append(b)
    arr[b].append(a)

#두가지 경우의 수 존재
#실내 시작 - 실내 끝 로만 구성된 경우의 수


stack = []
visited = [False]*(N+1)

answer = 0
for i in range(1, N+1):
    if gubun[i] == "1" and not visited[i]:
        stack.append(i)
        tmp = 1

        while stack:
            idx = stack.pop()
            visited[idx] = True
            for x in arr[idx]:
                if gubun[x] == "1" and not visited[x]:
                    tmp += 1
                    stack.append(x)

        tmp = (tmp-1)*2
        #print(tmp)
        answer += tmp

for i in range(1, N+1):
    if gubun[i] == "0" and not visited[i]:
        stack.append(i)
        tmp = 0

        while stack:
            idx = stack.pop()
            visited[idx] = True
            for x in arr[idx]:
                if gubun[x] == "1":
                    tmp += 1
                elif gubun[x] == "0" and not visited[x]:
                    stack.append(x)

        tmp = (tmp-1) * tmp
        #print(tmp)
        answer += tmp

print(answer)