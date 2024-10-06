import heapq
INF = (1e9)

def solution(N, road, K):
    answer = 0
    distance = [INF] * (N + 1)
    graph = [[] for _ in range(N + 1)]
    
    for edge in road:
        a, b, dist = edge
        graph[a].append([b, dist]) # a 마을에서 b 마을까지의 거리(양방향 이동 가능)
        graph[b].append([a, dist]) # b 마을에서 a 마을까지의 거리(양방향 이동 가능)
        

    q = []
    heapq.heappush(q, (0, 1)) 
    distance[1] = 0 # 시작 마을인 1번 마을에서 1번 마을까지의 거리는 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                            
    for dist in distance:
        if dist <= K:
            answer += 1

    return answer