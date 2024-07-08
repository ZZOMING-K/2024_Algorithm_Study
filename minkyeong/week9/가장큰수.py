def solution(numbers):
    answer_list = [[] for _ in range(len(numbers))]
    numbers = list(map(str , numbers)) 
    
    for idx , num in enumerate(numbers) :
        answer_list[idx].append(num)
        answer_list[idx].append(num*3)
    
    #정렬수행 
    answer_list.sort(key = lambda x : x[1] , reverse=True) 
    
    #차례대로 
    result = ''
    for answer in answer_list :
        result += answer[0]
    result = str(int(result))
    
    return result


#순열 이용 => 시간초과.. 
#from itertools import permutations
#def solution(numbers):
#     answer_list = []
    
#     res_list  = list(permutations(numbers , len(numbers)))
    
#     for res in res_list :
#         answer_list.append(''.join(map(str,res))) 
#     answer_list = sorted(set(answer_list) , reverse = True)
#     answer = answer_list[0]
#     return answer 