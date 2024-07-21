def solution(nums):
    answer = 0
    
    monsters = len(nums)
    unique_monsters = len(set(nums))
    
    if unique_monsters < monsters / 2:
        answer = unique_monsters
    else:
        answer = monsters // 2
    
    return answer