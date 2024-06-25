import sys
input = sys.stdin.readline

N = int(input().strip())
W = [list(map(int, input().split())) for _ in range(N)]
min_cost = float('inf')

def tsp(start, current, count, cost, visited):
    global min_cost
    if count == N and W[current][start] != 0:
        min_cost = min(min_cost, cost + W[current][start])
        return
    for i in range(N):
        if not visited[i] and W[current][i] != 0:
            visited[i] = True
            tsp(start, i, count + 1, cost + W[current][i], visited)
            visited[i] = False

for i in range(N):
    visited = [False] * N
    visited[i] = True
    tsp(i, i, 1, 0, visited)

print(min_cost)

