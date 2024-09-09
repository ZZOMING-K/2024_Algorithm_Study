#조이스틱 조작 횟수의 최솟값 return 
def solution(name):

    moves = 0
    #오른쪽으로만 커서를 이동할 때 거리 
    cur = len(name) -1 
    
    for i in range(len(name)) :
        #A에서 알파벳으로 이동(위쪽이동) , A->Z에서 알파벳으로 이동 (아래쪽이동)  
        moves += min(ord(name[i]) - ord('A') , ord('Z')-ord(name[i])+1)
        
        next_index = i+1 
        
        while next_index < len(name) and name[next_index] == 'A' :
            next_index +=1
            
            #현재 위치에서 처음으로 돌아가 왼쪽으로 가기  
            cur = min(cur , i + len(name)-next_index) 
    
    moves += cur         
    return moves