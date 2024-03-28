import sys

input = sys.stdin.readline
org = input().strip()
bomb = input().strip()

stack = []

for i in org:
    stack.append(i)

    if ''.join(stack[-len(bomb):]) == bomb:
        for i in range(len(bomb)):
            stack.pop()

answer = ''.join(stack)

if answer:
    print(answer)
else:
    print('FRULA')
