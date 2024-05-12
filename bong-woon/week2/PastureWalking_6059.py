n, q = map(int, input().split())

info = [list(map(int, input().split())) for _ in range(n-1)] # 입력 정보
graph = [dict() for _ in range(n + 1)] # n번 목장이 어떤 목장과 연결되어 있는지 정보


for i in range(1, n+1): # 1, 2, 3, 4, ..., n
    for val in info: # [2, 1, 2], [4, 3, 2], [1, 4, 3]
        if i in val[:2]:  # [2, 1], [4, 3], [1, 4]
            for node in val[:2]:
                if node != i: 
                    graph[i][node] = val[-1] # graph = [{}, {node : val[-1]}]
print(graph)

def dfs(graph, check, p1, p2, temp, total):
    check[p1] = True
    
temp = 0
total = 0

for _ in range(q):
    check = [False] * (n + 1) # 방문 여부 체크
    p1, p2 = map(int, input().split())
    ans = dfs(graph, check, p1, p2, temp, total)
    print(ans)
    print(check)