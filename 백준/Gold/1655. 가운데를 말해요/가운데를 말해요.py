import heapq
import sys
input = sys.stdin.readline


leftheap = [] #최대 힙
rightheap = [] #최소 힙

#leftheap과 rightheap의 [0]은 중간값이 되는 것이다!


N = int(input())

for i in range(1, N+1):
    number = int(input())
    
    if i % 2 != 0: #홀수일 때
        heapq.heappush(leftheap, -number)
    else: #짝수일 때
        heapq.heappush(rightheap, number)
    
    if rightheap and rightheap[0] < -leftheap[0]:
        lefttmp = -1 * heapq.heappop(leftheap)
        righttmp = heapq.heappop(rightheap)

        heapq.heappush(leftheap, -righttmp)
        heapq.heappush(rightheap, lefttmp)
    
    print(-leftheap[0])
            

