M = int(input())
tobefound = list(map(int, input().split()))

N = int(input())
tofind = list(map(int, input().split()))

tobefound.sort()

def binsearch(tofind, inlist):
    start = 0
    end = len(inlist) - 1
    target = (start + end) // 2

    while start <= end:
        if inlist[target] == tofind:
            return 1
        elif inlist[target] < tofind:
            start = target + 1
        else:
            end = target - 1

        target = (start + end) // 2
    return 0

for i in range(N):
    print(binsearch(tofind[i], tobefound))
