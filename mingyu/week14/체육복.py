def solution(n, lost, reserve):
    answer = 0
    for i in range(1, n + 1):
        if i in lost:
            if i in reserve:
                lost.remove(i)
                reserve.remove(i)
    for i in range(1, n + 1):
        if i in lost:
            if i - 1 in reserve:
                answer = answer + 1
                continue
            elif i + 1 in reserve:
                answer = answer + 1
                reserve.remove(i+1)
                continue
        else:
            answer = answer + 1
                
                
    return answer
