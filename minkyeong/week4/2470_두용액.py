#시간초과에러 발생 => 다시 풀이하겠습니다. 

n = int(input())
n_list = list(map(int, input().split()))

current = float('inf')
answer = None


N = int(input())
num_list = list(map(int,input().split())) 

#내림차순정렬 
num_list.sort(ascending = False)

start , end = 0 , len(num_list)-1  
point = abs(num_list[start] , num_list[end])


while start <= end :
    
    current_point = num_list[start] + num_list[end]
    
    if abs(current_point) < point :
        current_point = abs(current_point)
        if current_point == 1 :
            break
    if current_point < 0 :
        start += 1 
    else :
        end -= 1 

print(current_point[0] , current_point[1])



for i in range(len(n_list) - 1):
    for j in range(i + 1, len(n_list)):
        
        abs_sum = abs(n_list[i] + n_list[j])

        if abs_sum < current:
            current = abs_sum
            answer = (n_list[i], n_list[j])

print(answer[0], answer[1])