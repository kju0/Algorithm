import sys
input = sys.stdin.readline

N, K = map(int, input().split())

numlist = input().rstrip()


stack = [numlist[0]]

for i in range(1, len(numlist)):
    num = int(numlist[i])
    while K > 0 and len(stack) != 0 and int(stack[-1]) < num:
        stack.pop()
        K -= 1
    
    stack.append(numlist[i])
    

while K > 0:
    K -= 1
    stack.pop()

#print(stack)
print(int(''.join(stack)))
    
