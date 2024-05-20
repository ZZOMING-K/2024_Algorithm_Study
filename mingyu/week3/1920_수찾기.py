import sys
input = sys.stdin.readline
from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))
A.sort()

M = int(input())

for i in map(int, input().split()):
    insertLocation = bisect_left(A, i)
    if insertLocation == len(A):
        print('0')
    elif A[insertLocation] == i:
        print('1')
    else:
        print('0')
