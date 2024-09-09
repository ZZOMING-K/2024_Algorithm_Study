def solution(n, lost, reserve):
    new_lost = []
    new_reserve = []
    
    for l in lost:
        if l in reserve:
            reserve.remove(l)
        else:
            new_lost.append(l)
    
    for r in reserve:
        new_reserve.append(r)
    
    for r in new_reserve:
        if r - 1 in new_lost:
            new_lost.remove(r - 1)
        elif r + 1 in new_lost:
            new_lost.remove(r + 1)
    
    return n - len(new_lost)

