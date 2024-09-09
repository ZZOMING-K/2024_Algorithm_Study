def solution(n , lost , reserve) : 
    
    reserve_only  = set(reserve) - set(lost) #여벌이 있는 학생 (빌려줄 수 있는 학생)
    lost_only = set(lost) - set(reserve) #도난당한 학생 (여벌 체육복 X)
    
    #본인이 입을 수 있는 체육복이 있는 학생 번호 
    student = [ i+1 for i in range(n) if i+1  not in lost_only ]  
    
    count = len(student) #체육복을 입을 수 있는 학생 수 먼저 count 
    
    for r in reserve_only : #앞뒤로 빌려줄 수 있는경우에만 count 세기 
        f , b = r-1 , r+1 
        if f in lost_only :
            lost_only.remove(f) 
            count += 1 
        elif b in lost_only:
            lost_only.remove(b)  
            count += 1 
    return count 

