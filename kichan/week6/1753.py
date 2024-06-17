# 유튜브 참고

import sys
import heapq

INF = sys.maxsize

V, E = map(int, input().split()) # 노드개수, 간선개수
K = int(input())

edge = [[] for _ in range(V+1)]
dist = [INF] * (V+1)

for i in range(E):
    u,v,w = map(int, input().split())   # 시작점,도착점,길이
    edge[u].append([w,v]) # 도착점까지의 길이, 도착점

dist[K] = 0
heap = [[0,K]]

while heap:
    cw,cv = heapq.heappop(heap)
    if dist[cv] != cw: continue
    for nw, nv in edge[cv]:
        if dist[nv] > (cw+nw):
            dist[nv] = cw+nw
            heapq.heappush(heap, [dist[nv], nv])

for i in range(1, V+1):
    if dist[i] == INF:
        print('INF')
    else:
        print(dist[i])