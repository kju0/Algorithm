def solution(n):
    num_list = [i for i in range(600) if i % 3 != 0 and '3' not in str(i)]
    
    print(num_list)
    return num_list[n-1]