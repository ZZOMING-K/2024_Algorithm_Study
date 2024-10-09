from itertools import combinations

def is_prime(num):
    
    for i in range(2,int(num**0.5)+1):
        if num%i == 0:
            return False
    else:
        return True


def solution(nums):
    answer = 0
    
    
    for a,b,c in combinations(nums, 3):
        num = (a+b+c)
        
        if is_prime(num):
            answer += 1

    return answer