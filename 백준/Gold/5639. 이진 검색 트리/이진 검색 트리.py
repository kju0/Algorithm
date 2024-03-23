import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

arr = []

#개수 주어지지 않는 입력 처리
while True:
    try:
        arr.append(int(input().rstrip()))
    except:
        break

def postorder(start, end):
    #종료 조건
    if start > end:
        return
    
    idx = end + 1
    root = arr[start]

    for i in range(start+1, end+1):
        if root < arr[i]:
            idx = i
            break
    
    postorder(start+1, idx-1)
    postorder(idx, end)
    print(root)

postorder(0, len(arr)-1)