import itertools
import sys
input = sys.stdin.readline


N = int(input())

possible_list = itertools.permutations([i for i in range(1, 10)], 3)




for _ in range(N):
    q_number, s_ans, b_ans = map(int, input().split())
    
    answer_list = []
    
    for plist in possible_list:
        s, b = 0, 0
        for idx, num in enumerate(str(q_number)):
            if int(num) == plist[idx]:
                s += 1
            elif int(num) != plist[idx] and int(num) in plist:
                b += 1
        
        if s == s_ans and b == b_ans:
            answer_list.append(plist)
    
    possible_list = answer_list

print(len(possible_list))