def solution(operations):
    import heapq
    answer = []
    heap = []
    for i, operation in enumerate(operations):
        sign = operation[0]
        num = int(operation[2:])
        if sign == "I":
            heapq.heappush(heap, num)
        else:
            if not heap:
                continue
            if num == -1:
                heapq.heappop(heap)
            if num == 1:
                newheap = []
                while heap:
                    heapq.heappush(newheap, heapq.heappop(heap) * -1)
                heapq.heappop(newheap)
                while newheap:
                    heapq.heappush(heap, heapq.heappop(newheap) * -1)
    if not heap:
        return [0, 0]
    elif len(heap) == 1:
        return [heap[0], heap[0]]
    else:
        minvalue = heapq.heappop(heap)
        newheap = []
        while heap:
            heapq.heappush(newheap, heapq.heappop(heap) * -1)
        maxvalue = heapq.heappop(newheap) * -1
        return [maxvalue, minvalue]
