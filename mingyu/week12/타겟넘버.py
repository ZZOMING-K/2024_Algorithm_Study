def solution(numbers, target):
    answer = 0
    
    nowdict = {}
    nextdict = {}
    nowdict[0] = 1
    
    for i in range(len(numbers)):
        for key in nowdict.keys():
            #print(nowarr)
            add = key + numbers[i]
            sub = key - numbers[i]
            
            nextdict[add] = nextdict.get(add, 0) + nowdict[key]
            nextdict[sub] = nextdict.get(sub, 0) + nowdict[key]
        #print()
        nowdict = nextdict
        nextdict = {}
        
    return nowdict.get(target, 0)
