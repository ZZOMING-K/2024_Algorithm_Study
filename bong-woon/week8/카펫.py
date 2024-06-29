def solution(brown, yellow):
    answer = []
    
    area = brown + yellow
    
    for i in range(1, area + 1):
        if area % i == 0:
            if area // i >= i:
                w = area // i
                h = i
                
                if (w - 2) * (h - 2) == yellow:
                    answer.append(w)
                    answer.append(h)

    return answer