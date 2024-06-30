def solution(answers):
    
    answer = []
    rank = [-1,0,0,0]
    
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i in range(len(answers)):
        if s1[i%5] == answers[i]:
            rank[1] += 1
            
        if s2[i%8] == answers[i]:
            rank[2] += 1
            
        if s3[i%10] == answers[i]:
            rank[3] += 1
            
    for idx,ans in enumerate(rank):
        if ans == max(rank):
            answer.append(idx)
            
    return answer