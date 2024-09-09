def solution(routes):
    answer = 1
    routes.sort()
    start = routes[0][0]
    exit = routes[0][1]
    while routes:
        if routes[0][0] <= exit:
            if routes[0][1] <= exit:
                exit = routes[0][1]
        else:
            exit = routes[0][1]
            answer = answer + 1
        routes = routes[1:]
    return answer
