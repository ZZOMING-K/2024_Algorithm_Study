def solution(number, k):
    answer = []
    n = len(number)
    
    for num in number:
        
        while answer and answer[-1] < num and k>0:
            answer.pop()
            k -= 1
        answer.append(num)
    
    answer = answer[:n-k]
    answer = ''.join(answer)
        
    return answer