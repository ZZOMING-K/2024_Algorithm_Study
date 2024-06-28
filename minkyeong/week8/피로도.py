from itertools import permutations 

def solution(k, dungeons):
    
    arr = list(permutations(dungeons , len(dungeons))) 
    
    max_count = 0 
    
    for i in arr :
        count = 0 
        power = k
        for j in i :
            if j[0] <= power :
                power -= j[1]
                count += 1 
            else :
                break
            max_count = max(max_count , count)
    
    return max_count
