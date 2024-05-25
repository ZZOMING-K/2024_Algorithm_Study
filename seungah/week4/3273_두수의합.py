n = int(input())
num  = list(map(int, input().split()))
x = int(input())
num.sort()
L,R = 0, n-1
count = 0

while L < R:
    a = num[L] + num[R]
    if a == x:
        count += 1
        L += 1 
        R -= 1  
    elif a < x:
        L += 1
    else:
        R -= 1

print(count)