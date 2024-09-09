def solution(n, costs):
    answer = 0
    
    def find_parent(parent, x):
        if parent[x] != x:
            parent[x] = find_parent(parent, parent[x])
        return parent[x]
    
    def union_parent(parent, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
            
    
    parent = [0] * n
    for i in range(n):
        parent[i] = i
    print(parent)
    
    costs.sort(key = lambda x : x[2])
    
    for cost in costs:
        a, b, c = cost
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            answer += c
    
    print(parent)
    
    return answer