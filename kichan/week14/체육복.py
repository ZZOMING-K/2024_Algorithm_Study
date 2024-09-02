def solution(n, lost, reserve):
    answer = 0
    
    students = [1] * n
    
    for i in lost:
        students[i-1] -= 1
    for j in reserve:
        students[j-1] += 1
        
    for k in range(n):
        if students[k]==0:
            if k > 0 and students[k-1] > 1:
                students[k] += 1
                students[k-1] -= 1
                
            elif k < n-1 and students[k+1] > 1:
                students[k] += 1
                students[k+1] -= 1
                
            
    
    for x in students:
        if x >0:
            answer += 1
    
    return answer
