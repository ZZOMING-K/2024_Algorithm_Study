import heapq

INF = int(1e9)

n, d = map(int, input().split())
graph = [[] for _ in range(d + 1)]
distance = [INF] * (d + 1)

for i in range(d):
    graph[i].append((i + 1, 1)) # 0번 노드부터 1번 노드까지 거리를 1, 1번 노드부터 2번 노드까지 거리를 2, ..., d - 1번 노드부터 d번 노드까지 거리를 1

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

for _ in range(n):
    a, b, c = map(int, input().split())
    if b > d: # 목표 지점 d보다 멀리 도착하는 경우는 제외
        continue
    graph[a].append((b, c))

dijkstra(0)
print(distance[d])