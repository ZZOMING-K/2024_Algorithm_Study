def solution(routes):
    answer = 0
    
    routes.sort(key = lambda x : x[1])
    
    location = -30001
    
    for route in routes:
        if location < route[0]:
            location = route[1]
            answer += 1
            
    return answer