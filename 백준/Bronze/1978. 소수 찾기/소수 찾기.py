n = int(input())
arr = list(map(int, input().split()))

#에라토스테네스의 체
#2의 배수부터 배수인 수는 다 1로 바꿀 예정
#아직 0이 아닌 수의 배수만 판별

nlist = [0 for i in range(max(arr)+1)]
nlist[0], nlist[1] = 1, 1
for i in range(2, max(arr)+1):
    idx = 2
    if nlist[i] == 1:
        continue
    while i*idx <= max(arr):
        nlist[i*idx] = 1
        idx += 1

answer = 0
for i in range(n):
    if nlist[arr[i]] == 0:
        #print(arr[i])
        answer += 1
print(answer)