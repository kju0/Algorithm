import sys
input = sys.stdin.readline

input_str = list(input().rstrip().split('-'))


answer = 0

for idx in range(len(input_str)):
    input_str[idx] = list(map(int, input_str[idx].split("+")))
    input_str[idx] = sum(input_str[idx])

    if idx != 0:
        answer -= input_str[idx]
        continue
    answer = input_str[idx]
        
    

    #+로 모여져있음!
print(answer)