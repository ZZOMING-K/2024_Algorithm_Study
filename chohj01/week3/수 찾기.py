import sys
def bsearch(B, start, end):
    if start > end:
        return 0
    mid = int((start+end)/2)
    if A[mid] == B:
        return 1
    elif A[mid] > B:
        end = mid - 1
    else:
        start = mid + 1
    return bsearch(B, start, end)

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))
A.sort()
for i in B:
    start = 0
    end = len(A) - 1
    print(bsearch(i, start, end))