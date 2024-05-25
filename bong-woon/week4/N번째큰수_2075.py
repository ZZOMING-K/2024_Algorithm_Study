import heapq

n = int(input())
h_tree = []

for _ in range(n):
    for num in map(int, input().split()):
        if len(h_tree) < n:
            heapq.heappush(h_tree, num)
        else:
            if num > h_tree[0]:
                heapq.heappop(h_tree)
                heapq.heappush(h_tree, num)

print(heapq.heappop(h_tree))