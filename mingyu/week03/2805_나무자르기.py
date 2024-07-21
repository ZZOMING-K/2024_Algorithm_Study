#import time

N, M = map(int, input().split())
A = list(map(int, input().split()))

A.sort(reverse = True)
#print(A)


cnt = 0             ##가지고 갈 수 있는 나무의 길이
height = A[0]       ##베는 높이
index = 1           ##벨 수 있는 나무의 수

while cnt < M:
    height = height - 1

    if index != N :
        while A[index] > height:
            index = index + 1
            if index == N:
                break

    cnt = cnt + index

    #print(height, index, cnt)
    #time.sleep(0.5)

print(height)
