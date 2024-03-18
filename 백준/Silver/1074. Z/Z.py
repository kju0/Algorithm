import sys
sys.setrecursionlimit(10**6)

n, r, c = map(int, input().split())

def z(n, r, c):
    if n == 0:
        return 0
    
    half_size = 1 << (n - 1)  # 현재 크기의 반

    if r < half_size and c < half_size:
        return z(n - 1, r, c)  # 1사분면에 속할 경우
    elif r < half_size and c >= half_size:
        return half_size * half_size + z(n - 1, r, c - half_size)  # 2사분면에 속할 경우
    elif r >= half_size and c < half_size:
        return 2 * half_size * half_size + z(n - 1, r - half_size, c)  # 3사분면에 속할 경우
    else:
        return 3 * half_size * half_size + z(n - 1, r - half_size, c - half_size)  # 4사분면에 속할 경우

print(z(n, r, c))
