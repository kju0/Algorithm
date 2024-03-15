T = int(input())
arr = []
for i in range(T):
    arr.append(int(input()))

max_arr = max(arr)

nlist = [0 for i in range(max_arr+1)]

for i in range(2, max_arr+1):
    if nlist[i] == 1:
        continue
    idx = 2
    while i*idx <= max_arr:
        nlist[i*idx]=1
        idx+=1


for i in range(T):
    target = arr[i]
    answer = []
    a = False
    for x in range(target//2, 1, -1):
        if nlist[x] != 0:
            continue
        for y in range(target//2, target):
            if nlist[y] != 0:
                continue
            if x + y > target:
                break
            if x + y == target:
                print(x, y)
                a = True
                break
        if a:
            break