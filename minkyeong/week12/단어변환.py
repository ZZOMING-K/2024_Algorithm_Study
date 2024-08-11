from collections import deque 

def solution(begin , target , words) : 
    #단어 비교 함수 
    def isValid(cur_v , next_v) : 
        count = 0 
        
        for i in range(len(cur_v)) : 
            if cur_v[i] != next_v[i] :  #만일 철자가 다를 경우 count +1 
                count+= 1 
        
        if count == 1 :
            return True  # 한 글자만 다를 경우 True 반환 
        else :
            return False # 이외 False 반환 
    
    visited = [False] * len(words)  # 방문 리스트 생성 

    q= deque()  #큐 생성 

    for i in range(len(words)) : 
        
        if isValid(begin , words[i]) :
            q.append( (words[i], 1))  #만일 시작하는 단어와 한글자만 다른 단어가 있을 경우 큐에 추가 (이때 dist는 1로 시작)
         
            
    while q : #큐가 빌때까지 반복 
        cur_w , dist = q.popleft()
        
        if cur_w == target : 
            return dist
        
        for i in range(len(words)) :
            if not visited[i] and isValid(cur_w , words[i]) : #현재 단어와 한글자만 다르고, 만일 방문하지 않았다면 방문 예약 및 큐에 추가  
                visited[i] = True
                q.append((words[i] , dist+1)) 
    
    return 0 

