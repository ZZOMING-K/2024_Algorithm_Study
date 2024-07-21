import sys
import heapq
#import time
input = sys.stdin.readline

N, M = map(int, input().split())

length = [{} for j in range(N + 1)] #입력값이 저장될 배열
fix = [set() for i in range(N + 1)]

for i in range(N + 1):
    length[i][i] = 0
    fix[i].add(i)

for i in range(M):
    a, b = map(int, input().split())
    length[a][b] = 1
    length[b][a] = 1



for i in range(N + 1):
    heap = []
    for j in length[i]:
        if j == i:
            continue
        else:
            heapq.heappush(heap, [length[i][j], j])
    while heap:
        now = heapq.heappop(heap)
        if now[1] in fix[i]:
            continue
        else:
            length[i][now[1]] = now[0]
            fix[i].add(now[1])
            for j in length[now[1]]:
                if length[now[1]][j] == 0:
                    continue
                else:
                    heapq.heappush(heap, [length[i][now[1]] + length[now[1]][j], j])

answer = [99999, 0]
for i in range(1, N+1):
    tmp = 0
    for j in range(1, N+1):
        tmp = tmp + length[i][j]
    if tmp < answer[0]:
        answer = [tmp, i]
print(answer[1])
