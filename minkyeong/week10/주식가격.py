def solution(prices):
    
    seconds = [0 for _ in range(len(prices))]
    
    stack = []
    for idx , price in enumerate(prices) :
        
        while stack and price < prices[stack[-1]] :
            end = stack.pop() 
            seconds[end] = idx - end 
        
        stack.append(idx)
        
        if seconds[idx] == 0 : #만일 주식가격이 떨어지지 않는다면
            seconds[idx] = len(prices) - (idx + 1)
    
    return seconds
        
        
        
        
        

        
        
        
        
        
