from itertools import permutations
import math 

# 정리해야될 개념 : 순열, 조합 라이브러리 , 소수 구하기 (소수 개수 구하기)

def solution(numbers):
    
    answer = 0
    
    #일단 numbers를 숫자 한개씩으로 분리(str로 입력됨) 
    number_li = []
    for num in numbers : 
        number_li.append(num)
        
    num_li = []
    #순열라이브러리 이용하여 나올 수 모든 수를 구하기 
    for i in range(1, len(number_li)+1) :
        new_num = list(permutations(number_li , i))
        for p in new_num : 
            new_num = (''.join(map(str,p)))
            if new_num[0] == '0' and len(new_num) >= 2 : #만일 숫자의 길이가 2이상이고, 첫번째 숫자가 0일 경우 0은 제거해주기 
                new_num = int(new_num[1:])
            new_num = int(new_num)
            num_li.append(new_num) 
        
    num_li = list(set(num_li)) #같은 숫자 중복제거 
    
    def is_prime(num) : #소수판단 함수 작성 
        if num == 0 or num == 1 : #만일 숫자가 0이나 1이면 소수가 아님 
            return False
        for i in range(2 , int(math.sqrt(num)) +1 ) :
            if num % i == 0 : #만일 나누어 떨어지는 경우 소수가 아님 
                return False
        return True #위 해당 사항이 모두 없을 경우 소수로 판단 
    
    for num in num_li :
        if is_prime(num) :
            answer += 1 #소수일경우 count 세기 
            
    return answer
