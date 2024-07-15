from collections import deque

def solution(priorities, location):

    queue = deque([]) 
    
    for idx , value in enumerate(priorities) :
        queue.append([idx , value]) 
    
    max_rank = max(priorities)
    answer = []
    
    while queue : #큐가 빌때까지 반복  
        
        for i , v in list(queue) :
            
            if v == max_rank :
                answer.append(i)
                queue.popleft() #꺼내서 answer 리스트에 추가  
                priorities.remove(v)
                
                if len(priorities) > 0 : 
                    max_rank = max(priorities) #max값 업데이트
            else :
                queue.popleft() #꺼내서 젤 뒤에 append하기 
                queue.append([i,v])
        
    for index , num in enumerate(answer) :
        if num == location :
            result = index+1 
            break
    
    return result 
        
            
            
        
        
        

        
    
        
