def solution(s):
    
    s_list = [] 
    
    for ss in s: 
        
        if (len(s_list) > 0)  and (s_list[-1] == '(') and (ss == ')') :
            s_list.pop()
        else : 
            s_list.append(ss)  
    
    if s_list :
        answer = False
    else :
        answer = True  
    return answer 


    