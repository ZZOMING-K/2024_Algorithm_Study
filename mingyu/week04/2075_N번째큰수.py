import heapq

N = int(input())

min_heap = []               

for i in range(N):
    for j in map(int, input().split()):

        if len(min_heap) >= N :
            heapq.heappush(min_heap, j)
            heapq.heappop(min_heap)

        else:
            heapq.heappush(min_heap, j)

print(heapq.heappop(min_heap))
