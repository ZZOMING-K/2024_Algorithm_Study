#어떤 숫자에서 K개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자 구하기 
#ex) 1924애서 수 2개를 제외 > 19 12 14 92 94 24 > 94 
#숫자와 제거할 개수가 주어질 때 만들 수 있는 수 중 가장 큰 수 구하기 > 첫번째로 오는 숫자가 가장 커야 함.

from itertools import combinations  #조합함수 사용 

#number = "4177252841"
#k = 4 
#return = "3234" 

def solution(number , k ) : 
    #첫 자리로 올 수 있는 숫자 범위 
    select = len(number)-k
    max_index = number[:select].index(max(number[:select])) #첫번째 자리로 올 수 있는 숫자 중 가장 큰 수 인덱스 추출 


    #range(max_index , len(number)) 에서 무작위로 select 개수 만큼 선택  > 가장 큰 수 인덱스로 부터 마지막 수 중에서 올 수 있는 숫자 구하기 (조합이용)
    li = list(combinations(number[max_index:], select))

    max_num = 0 
    for num in li :
        join_num = ''.join(num) 
        max_num = max(max_num  , int(join_num))

    return max_num


