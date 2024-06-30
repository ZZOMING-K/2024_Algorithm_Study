from itertools import permutations

def is_prime_number(x) :
    if x < 2 :
        return False
    
    for i in range(2, x) :
        if x % i == 0 :
            return False
            
    return True


def solution(numbers):
    answer = 0
    num = []
    nums=[]
    numbers = list(numbers)
    
    for i in range(1,len(numbers)+1):
        num.append(list(set(map(''.join, permutations(numbers,i)))))
    
    for l in num:
        for k in l:
            nums.append(int(k))
    nums = list(set(nums))
    
    for j in nums:
        if is_prime_number(j) == True:
            answer += 1
    
    return answer