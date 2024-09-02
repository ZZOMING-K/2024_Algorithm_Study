def solution(routes):
    answer = 0
    now = -30001
    
    routes = sorted(routes, key = lambda x : x[1])
    
    for start, end in routes:
        if now < start:
            now = end
            answer += 1
    
    
    return answer