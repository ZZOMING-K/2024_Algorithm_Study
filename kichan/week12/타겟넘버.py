def solution(numbers, target):
    result = [0]
    
    for num in numbers:
        temp = []
        
        for res in result:
            temp.append(res + num)
            temp.append(res - num)
    
        result = temp
        
    cnt = 0
        
    for i in result:
        if i == target:
            cnt += 1
    
    return cnt