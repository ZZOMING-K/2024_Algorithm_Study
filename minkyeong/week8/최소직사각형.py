def solution(sizes):

    # 아이디어
    # 1. 만일 세로 길이가 가로길이보다 길다면 바꾸기 (세로길이보다 가로길이가 더 길게 설정)
    # 2. 최대 세로 길이 * 최대 가로 길이 = 모든 명험커버 가능 

    max_w ,max_h = 0 ,0
    # 만일 가로길이가 세로길이보다 길다면 바꾸기 
    for size in sizes : 
        if size[0] <= size[1] :
            size[0] , size[1] = size[1],size[0]
        
        max_w = max(size[0] , max_w) #가로 최대 길이 값 업데이트 
        max_h = max(size[1] , max_h) #세로 최대 길이 값 업데이트 
    # 최대 가로길이 x 최대 세로길이 = 모든 명함들 수납이 가능
    answer = max_w * max_h
    
    return answer