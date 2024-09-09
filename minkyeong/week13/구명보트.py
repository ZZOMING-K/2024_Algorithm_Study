#최대 2명 
def solution(people, limit):
    answer = 0 
    people = sorted(people, reverse = True) 
    #가장 무거운 사람과 가장 가벼운 사람을 같이 태우기
    right = len(people) - 1 
    left = 0  
    
    while left <= right : 
        if people[right] + people[left] <= limit :
            right -= 1 
            left += 1 
            answer += 1
        else :
            left += 1 
            answer +=1

    return answer



          

             
