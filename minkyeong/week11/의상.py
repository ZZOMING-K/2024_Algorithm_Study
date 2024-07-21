from collections import defaultdict

def solution(clothes):
    
    comb = {}
    
    for cl in clothes : 
        comb.get(comb[cl[1]] , [])
        comb[cl[1]].append(cl[0]) 
    
    count = 1 
    for key in comb: 
        count *= (len(comb[key])+1)
    count -= 1
    
    return count