import heapq

INF = (1e9)

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

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

lst = [] # 케빈 베이컨의 수를 저장할 리스트
for i in range(1, n + 1):
    dijkstra(i)
    kevin_score = 0
    for j in distance[1:]: # distance[0] = INF이므로 제외하고 확인
        kevin_score += j
    
    lst.append(kevin_score)
    distance = [INF] * (n + 1) # dijkstra 함수를 실행하면서 갱신된 distance를 다시 INF로 초기화
    
print(lst.index(min(lst)) + 1) # 최솟값이 여러 개 있을 경우 가장 앞쪽에 위치한 최솟값을 찾는다.