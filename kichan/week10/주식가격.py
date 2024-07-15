def solution(prices):
    n = len(prices)
    answer = [0 for _ in range(n)]
    price_check = []
    
    for idx,price in enumerate(prices):
        if len(price_check)>0 and price<price_check[-1][1]:
            for back_idx, back_price in price_check[::-1]:
                if back_price > price:
                    answer[back_idx] = (idx-back_idx)
                    price_check.pop()
        
        price_check.append((idx,price))
    
    for idx,_ in price_check:
        answer[idx] = n-idx-1
    
    return answer