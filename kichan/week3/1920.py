# 1920

import sys

n = int(input())
a = list(map(int, sys.stdin.readline().split()))
m = int(input())
b = list(map(int, sys.stdin.readline().split()))

a.sort()

def binary_func(a,b):

    start = 0
    end = len(a)-1

    while start <= end:
        mid = (start+end) // 2
        
        if b == a[mid]:         # 바로 찾았다면 1출력
            return 1
        
        elif b > a[mid]:
            start = mid +1
        
        else:
            end = mid -1
    return 0                    # 존재하지 않으면 0출력

for i in range(m):
    print(binary_func(a,b[i]))