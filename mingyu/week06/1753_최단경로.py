#가장 가까운 간선부터 차례대로 고정
#import time
import sys
input = sys.stdin.readline
import heapq


V, E = map(int, input().split())
start = int(input())

length = [{} for j in range(V + 1)] #입력값이 저장될 배열
fix = set()
fix.add(start)
heap = []


for i in range(V+1):
    length[i][i] =  0


for i in range(E):
    a, b, l = map(int, input().split())
    if l < length[a].get(b, 11):
        length[a][b] = l
#print(length)
#print(fix)



for i in length[start]:
    if i == start:
        continue
    else:
        heapq.heappush(heap, [length[start][i], i])


while heap:
    #print(heap)
    #print(fix)
    now = heapq.heappop(heap)
    if now[1] in fix:
        continue
    else:
        length[start][now[1]] = now[0]
        fix.add(now[1])
        for i in length[now[1]]:
            if length[now[1]][i] == 0:
                continue
            heapq.heappush(heap, [length[start][now[1]] + length[now[1]][i], i])

for i in range(1, V+1):
    print(length[start].get(i, 'INF'))


