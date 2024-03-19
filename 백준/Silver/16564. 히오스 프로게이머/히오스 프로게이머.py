import sys
input = sys.stdin.readline

n, k = map(int, input().split())
score = [0]*n

for i in range(n):
    score[i] = int(input())

score.sort()
#print(score)

#mid가 값임
start = score[0]
end = score[0] + k

result = 0
while start <= end:
    mid = (start+end)//2

    hap = 0
    for i in range(n):
        if score[i] < mid:
            hap += mid - score[i]
    
    if hap <= k:
        start = mid + 1
        result = max(mid, result)
    else:
        end = mid - 1

print(result)





