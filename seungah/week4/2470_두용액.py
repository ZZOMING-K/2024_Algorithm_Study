N = int(input())
liquids = list(map(int, input().split()))
liquids.sort()
L,R = 0, N-1
last = float('inf')
closetozero = (0,0)

while L < R:
    a = liquids[L] + liquids[R]

    if abs(a) < last:
        last = abs(a)
        closetozero = (liquids[L], liquids[R])
    if a == 0:
        break
    elif a > 0:
        R -= 1
    else:
        L += 1

print(*closetozero)
