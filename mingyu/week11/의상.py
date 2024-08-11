def solution(clothes):
    from itertools import combinations
    answer = 0

    matching = {}
    outfit = {}
    
    for i, cloth in enumerate(clothes):
        name = cloth[0]
        part = cloth[1]

        if matching.get(part, 0) == 0:
            matching[part] = len(list(matching.keys())) + 1
        part = matching[part]
        
        if outfit.get(part, 0) == 0:
            outfit[part] = [1]
        else:
            outfit[part].append(outfit[part][-1] + 1)
    #print(outfit)
    partnum = len(list(outfit.keys()))
    #print(partnum)
    combarr = [i+1 for i in range(partnum)]
    
    for i in range(partnum):
        sumNum = 0
        for j in combinations(combarr, i + 1):
            #print(j)
            subsum = 1
            for k in j:
                subsum = subsum * len(outfit[k])
            sumNum = sumNum + subsum
        #print(i + 1, sumNum)
        answer = answer + sumNum
    

    
    return answer
