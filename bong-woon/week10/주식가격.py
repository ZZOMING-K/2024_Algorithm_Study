from collections import deque

def solution(prices):
    answer = []
    
    price_q = deque(prices)
    
    while price_q:
        count = 0
        current_price = price_q.popleft()
        
        for price in price_q:
            if current_price <= price:
                count += 1
            else:
                count += 1
                break
                
        answer.append(count)
    return answer