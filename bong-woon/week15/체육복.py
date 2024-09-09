def solution(n, lost, reserve):
    answer = 0
    
    lost.sort()
    reserve.sort()
	
    for los in lost[:]:
        if los in reserve:
            lost.remove(los)
            reserve.remove(los)
	
    for res in reserve:
        if res - 1 in lost:
            lost.remove(res - 1)
        elif res + 1 in lost:
            lost.remove(res + 1)
    
    answer = n - len(lost)
    return answer