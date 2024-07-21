def solution(nums): 
    num = len(nums) // 2 
    pocketmon = set(nums)
    answer = min(num , len(pocketmon))
    return answer