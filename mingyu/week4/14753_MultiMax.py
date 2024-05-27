import heapq
max_heap = []
min_heap = []

N = int(input())
for i in map(int, input().split()):
    heapq.heappush(min_heap, i)
    heapq.heappush(max_heap, i * -1)

bigFirst = heapq.heappop(max_heap) * -1
bigSecond = heapq.heappop(max_heap) * -1
bigThird = heapq.heappop(max_heap) * -1

smallFirst = heapq.heappop(min_heap)
smallSecond = heapq.heappop(min_heap)

case1 = bigFirst * bigSecond * bigThird
case2 = bigFirst * bigSecond
case3 = smallFirst * smallSecond * bigFirst
case4 = smallFirst * smallSecond

print(max(case1, case2, case3, case4))