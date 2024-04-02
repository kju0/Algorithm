import sys
input = sys.stdin.readline

#멀티탭 스케쥴링

N, K = map(int, input().split())

if N >= K:
    print(0)
    exit()


arr = list(map(int, input().split()))

#플러그를 뽑아야 할 상황에서 플러그에서 가장 늦게 나오거나 안 나오는 용품 빼주기
answer = 0
plug = []

#플러그 길이가 N보다 작거나 같으면
#플러그에 지금 꽂으려는 용품이 있는지 검사
#없으면 플러그에서 뺄 값 검사 - 일단 remove(인덱스)로 빼주기
#뺄 값 검사할 때는 가장 안 나오는 용품 혹은 가장 늦게 나오는 콘센트를 빼주기

for i in range(K):
    if arr[i] in plug:
        continue

    #plug에 용품은 없지만 plug 자리가 비어 있는 경우
    if len(plug) < N:
        plug.append(arr[i])
        continue

    rm_idx, late_idx = 0, 0

    for p in plug:
        if p not in arr[i:]:
            rm_idx = p
            break

        elif arr[i:].index(p) > late_idx:
            late_idx = arr[i:].index(p)
            rm_idx = p
    
    answer += 1
    plug[plug.index(rm_idx)] = arr[i]


print(answer)