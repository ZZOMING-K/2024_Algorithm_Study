from collections import deque

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))

queue = deque([])
for i in range(N):
     if A[i] == 0:
        queue.appendleft(B[i])


for i in range(M):
  queue.append(C[i])
  print(queue.popleft(), end = " ")