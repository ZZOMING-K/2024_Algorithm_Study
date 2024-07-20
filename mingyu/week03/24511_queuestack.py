from collections import deque

N = input()
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = input()
C = list(map(int, input().split()))

queue = deque()

for i in range(len(A)):
    if A[i] == 0:
        queue.append(B[i])

for i in C:
    queue.appendleft(i)
    print(queue.pop(), end = ' ')
