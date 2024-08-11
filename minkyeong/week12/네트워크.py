def solution(n, computers):
    #인접행렬을 인접리스트로 변환 
    graph = [[] for i in range(n)]
    for i in range(n) :
        for j in range(n) : 
            if computers[i][j] == 1 :
                graph[i].append(j)
    
    visited = [False] * len(graph)
    
    #dfs 함수 정의 
    def dfs(graph, cur_v, visited) : 
        for next_v in graph[cur_v] : 
            if not visited[next_v] :
                visited[next_v] = True
                dfs(graph , next_v, visited)
    
    count = 0
    
    
    for idx , v in enumerate(visited) :
        if v == False :
            dfs(graph , idx , visited)
            count += 1 
            
    return count