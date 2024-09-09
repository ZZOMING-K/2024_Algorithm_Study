import heapq

def solution(operations):
    heap = []
    
    for o in operations:
        ID,num = o.split()
        if ID == 'I':
            heap.append(int(num))
        else:
            if num == '-1' and len(heap) >= 1:
                heapq.heappop(heap)
            
            elif num == '1' and len(heap) >= 1:
                heap.sort()
                heap.pop()
    
    if len(heap) == 0:
        answer = [0,0]
    
    else:
        answer = [max(heap), min(heap)]
    
    
    return answer