def solution(nums):
    answer = 0
    
    choice = len(nums)//2
    s_n = len(set(nums))
    
    if s_n >= choice:
        return choice
    
    elif s_n < choice:
        return s_n