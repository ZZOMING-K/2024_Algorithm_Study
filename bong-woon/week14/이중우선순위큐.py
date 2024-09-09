import heapq

def solution(operations):
    heap = []
    
    for operation in operations:
        current_operation = operation.split()
        number = int(current_operation[1])

        if current_operation[0] == "I":
            heapq.heappush(heap, number)

        else:
            if len(heap) == 0:
                pass
            elif current_operation[1] == "1":
                max_value = heapq.nlargest(1, heap)[0]
                heap.remove(max_value)
            elif current_operation[1] == "-1":
                heapq.heappop(heap)
        
        if heap:
            answer = [heapq.nlargest(1, heap)[0], heapq.nsmallest(1, heap)[0]]
        else:
            answer = [0, 0]

    return answer