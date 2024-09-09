import sys
import heapq

input = sys.stdin.read
data = input().split()

V = int(data[0])
E = int(data[1])
K = int(data[2])

G = [[] for _ in range(V + 1)]
idx = 3
for _ in range(E):
    u = int(data[idx])
    v = int(data[idx + 1])
    w = int(data[idx + 2])
    G[u].append((v, w))
    idx += 3

dist = [float('inf')] * (V + 1)
dist[K] = 0
pq = [(0, K)]

while pq:
    cur_d, cur = heapq.heappop(pq)

    if cur_d > dist[cur]:
        continue

    for next, w in G[cur]:
        d = cur_d + w
        if d < dist[next]:
            dist[next] = d
            heapq.heappush(pq, (d, next))

for i in range(1, V + 1):
    if dist[i] == float('inf'):
        print('INF')
    else:
        print(dist[i])
