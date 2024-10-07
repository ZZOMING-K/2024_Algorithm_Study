def solution(A, B):
    answer = 0
    
    A.sort(reverse=True)
    B.sort(reverse=True)
    
    for i in range(len(A)):
        if B[i] > A[i]:
            answer += 1
        
    
    return answer