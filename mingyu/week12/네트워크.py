def solution(n, computers):
    
    def bfs(nowArr, computers, returnArr):
        if not nowArr:
            return returnArr
        
        nextArr = set()
        while nowArr:
            now = nowArr.pop()
            returnArr.append(now)
            for i, computer in enumerate(computers[now]):
                if computer == 1 and i not in returnArr:
                    nextArr.add(i)
                    returnArr.append(i)
                    
        return bfs(list(nextArr), computers, returnArr)
                
        
    
    answer = 0
    
    checked = []
    
    for i in range(len(computers)):
        if i in checked:
            continue
        else:
            answer = answer + 1
            checked.extend(bfs([i], computers, [i]))
            
    
    return answer
