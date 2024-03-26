import heapq
import sys
input = sys.stdin.readline

n = int(input())

people = [[0, 0] for _ in range(n)]
for i in range(n):
    people[i][0], people[i][1] = map(int, input().split())

    if people[i][0] > people[i][1]:
        tmp = people[i][0]
        people[i][0] = people[i][1]
        people[i][1] = tmp


train = int(input())

#print(people)

minPeople = []
#train 길이보다 긴 사람은 빼주기
for i in range(n):
    if train >= people[i][1]-people[i][0]:
        minPeople.append([people[i][0], people[i][1]])

#print(minPeople)

minPeople.sort(key=lambda x:x[1])
#print(minPeople)

hq = []
max_ans = 0
#끝점을 기준으로 포함되는 사람은 추가해주고, 빼주기
for i in range(len(minPeople)):
    heapq.heappush(hq, [minPeople[i][0], minPeople[i][1]])
    if len(hq) >= 2 and minPeople[i][1] - hq[0][0] > train:
        heapq.heappop(hq)
    max_ans = max(max_ans, len(hq))

print(max_ans)


    
