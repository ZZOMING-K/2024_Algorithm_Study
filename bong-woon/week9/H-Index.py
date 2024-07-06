def solution(citations):
    answer = 0
    max_h = len(citations)
    
    while True:
        count = 0
        for num in citations:
            if num >= max_h:
                count += 1
    
        if count >= max_h:
            answer = max_h
            break
        else:
            max_h -= 1
            
    return answer