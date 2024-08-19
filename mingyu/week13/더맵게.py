def solution(scoville, K):
    import heapq
    heap = []
    
    for i in scoville:
        heapq.heappush(heap, i)
    
    if heap[0] >= K:
        return 0
    
    answer = 0
    
    while len(heap) >= 2:
        
        answer = answer + 1
        
        menu1 = heapq.heappop(heap)
        menu2 = heapq.heappop(heap)
        mix = menu1 + 2 * menu2
        heapq.heappush(heap, mix)
        
        if heap[0] >= K:
            return answer
        
    return -1
