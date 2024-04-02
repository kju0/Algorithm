import heapq
import sys
input = sys.stdin.readline

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
#동호가 받을 수 있는 최대 컵라면 수는?

#그리디
#print(arr)

#데드라인 오름차순
#컵라면 수 내림차순

arr.sort(key=lambda x:(x[0], -x[1]))

#print(arr)
#데드라인 기준으로 넣을 수 있다고 다 넣으면 안된다!
#데드라인이 더 큰 값 중에 데드라인이 적은 일보다 더 큰 컵라면 수를 가진 값 가능

hq = []
answer, cnt = 0, 1

for i in range(N):
    if cnt <= arr[i][0]:
        answer += arr[i][1]
        heapq.heappush(hq, [arr[i][1],arr[i][0]])
        cnt += 1
    elif len(hq) != 0 and hq[0][0] < arr[i][1]:
        tmp = heapq.heappop(hq)
        answer -= tmp[0]
        heapq.heappush(hq, [arr[i][1], arr[i][0]])
        answer += arr[i][1]

print(answer)

