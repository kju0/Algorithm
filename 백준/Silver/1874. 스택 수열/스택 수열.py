import sys
input = sys.stdin.readline

N = int(input())

ans, stack = [], []

n = 1

for _ in range(N):
    num = int(input())

    while n <= num:
        stack.append(n)
        ans.append('+')
        n += 1

    if stack[-1] == num:
        stack.pop()
        ans.append('-')

    else:
        ans = False
        break

if not ans:
    print("NO")
else:
    for i in range(len(ans)):
        print(ans[i])