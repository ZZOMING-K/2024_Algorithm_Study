def solution(sizes):
    answer = 0
    for size in sizes:
        if size[0] < size[1]:
            size[0], size[1] = size[1], size[0] # 길이가 큰 쪽을 가로라고 생각
    
    width_max = 0
    height_max = 0
    for size in sizes:
        if size[0] > width_max:
            width_max = size[0]
        if size[1] > height_max:
            height_max = size[1]
    
    answer = width_max * height_max
    return answer