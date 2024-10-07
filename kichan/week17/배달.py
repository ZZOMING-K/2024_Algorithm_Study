import heapq

def solution(N, road, K):
    answer = 0
    
    path = [[] for _ in range(N+1)]
    
    # 각 마을 경로,가중치 계산
    for r in road:
        start, end ,time = r[0], r[1], r[2]
        path[start].append([end,time])
        path[end].append([start,time])
    
    # 각 마을까지의 최대 시간 계산
    distances = [float('inf')] * (N+1)
    distances[1] = 0
    
    # (time, village)
    heap = [(0,1)]
    
    while heap:
        current_distance, current_village = heapq.heappop(heap)
        
        for neighbor, travel_time in path[current_village]:
            distance = current_distance + travel_time
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))
    
    answer = sum(1 for d in distances if d <= K)
        
    
    return answer