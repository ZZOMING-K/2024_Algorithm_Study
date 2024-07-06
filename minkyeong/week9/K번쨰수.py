def solution(array, commands):
    #i부터 j까지 자르기 
    #자른 배열 정렬 후 k번째 숫자 return 
    
    answer = []
    for command in commands :
        i , j , k = command[0] , command[1] , command[2] 
        res = sorted(array[i-1:j])[k-1]
        answer.append(res)
    return answer