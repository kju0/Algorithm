k = int(input())

arr0 = [0]*6
arr1 = [0]*6

for i in range(6):#육각형
    a, b = map(int, input().split())

    arr0[i] = a
    arr1[i] = b


arr0 = arr0 + arr0
arr1 = arr1 + arr1
#print(arr0)

#2개씩 나눠서 확인
for i in range(6):
    if arr0[i:i+2] == arr0[i+2:i+4]:
        #print(i)
        #print(arr1[i], arr1[i+1], arr1[i+2], arr1[i+3])
        break

print((arr1[i+4]*arr1[i+5] - arr1[i+1]*arr1[i+2])*k)


