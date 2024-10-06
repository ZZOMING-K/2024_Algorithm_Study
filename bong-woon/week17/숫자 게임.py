def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    
    n = len(A)
    idx_a = 0
    idx_b = 0
    
    while idx_a < n and idx_b < n: # A, B의 인덱스가 둘다 n보다 작은 동안 계속 반복
        if B[idx_b] > A[idx_a]: # B의 점수가 A의 점수보다 크면 
            answer += 1 # B팀의 점수 + 1
            idx_a += 1 # 그 다음 A팀의 사원
            idx_b += 1 # 그 다음 B팀의 사원
        else: # B의 점수가 A의 점수보다 작다면
            idx_b += 1 # B의 인덱스를 증가시켜서 더 큰 값을 가져와서 비교
    return answer