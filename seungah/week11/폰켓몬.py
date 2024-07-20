def solution(nums):
    
    ponketmonnum = set(nums)
    nu_dup = len(nums) // 2
    return min(len(ponketmonnum), nu_dup)