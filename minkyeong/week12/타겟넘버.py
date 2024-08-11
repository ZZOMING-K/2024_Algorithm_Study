def solution(numbers , target) : 

    result = [0] 
    answer = []

    for number in numbers : 
        for r in result : 
            answer.append(r + number) #더하기 연산
            answer.append(r - number) #빼기 연산  
            result = answer #result를 연산 결과로 업데이트 
        answer = [] #answer 초기화 

    count = 0 

    #Target과 같은 숫자 찾기 
    for i in result : 
        if i == target :
            count += 1 
    
    return count 
