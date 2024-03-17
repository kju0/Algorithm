import sys
input = sys.stdin.readline

w, h = map(int, input().split())
n = int(input())

width, height = [0, w], [0, h]
for _ in range(n):
    idx, point = map(int, input().split())
    if idx == 0:
        height.append(point)
    else:
        width.append(point)

width.sort()
height.sort()

max_width, max_height = 0, 0

for i in range(len(width)-1):
    if max_width < abs(width[i]-width[i+1]):
        max_width = abs(width[i]-width[i+1])

for i in range(len(height)-1):
    if max_height < abs(height[i]-height[i+1]):
        max_height = abs(height[i]-height[i+1])

print(max_width*max_height)


