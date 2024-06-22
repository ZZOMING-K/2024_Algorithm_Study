N, M = map(int, input().split())
graph = [[100] * N for _ in range(N)]  # 올바른 그래프 초기화
relation = []

for i in range(N):
    graph[i][i] = 0

for _ in range(M):
    friend1, friend2 = map(int, input().split())
    friend1 -= 1  
    friend2 -= 1  
    relation.append((friend1, friend2))
    graph[friend1][friend2] = 1
    graph[friend2][friend1] = 1

# 플로이드-워셜 알고리즘
for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

total = N * 100
count = 0
for i in range(N):
    if sum(graph[i]) < total:
        total = sum(graph[i])
        count = i + 1 

print(count)