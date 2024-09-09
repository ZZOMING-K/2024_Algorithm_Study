def solution(routes):
    routes.sort(key=lambda x: x[1])
    answer = 0
    last_camera_position = -30001  
    for route in routes:
        if last_camera_position < route[0]:
            answer += 1
            last_camera_position = route[1]  
    
    return answer
