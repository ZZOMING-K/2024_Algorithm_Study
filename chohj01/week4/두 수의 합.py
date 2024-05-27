import sys

n = int(sys.stdin.readline())
alist = list(map(int, sys.stdin.readline().split()))
res = int(sys.stdin.readline())

alist.sort()

tu = 0
left, right = 0, n-1

while left < right:
    temp = alist[left] + alist[right]
    if temp == res:
        tu += 1
        left +=1
    elif temp < res:
        left +=1
    else:
        right-=1

print(tu)