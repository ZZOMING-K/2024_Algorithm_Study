n = int(input()) #수열의 크기 
num_list = list(map(int,input().split())) #수열에 포함되는 수 
x = int(input()) # 자연수를 더했을 때 만족해야하는 수 

#오름차순 정렬  
num_list.sort()


count = 0

start , end = 0 , len(num_list)-1 


while start < end : 
    

    if num_list[start] + num_list[end] > x :
        end = end - 1 
        
        
    elif num_list[start] + num_list[end] < x :
        start = start +1
        
    else :
        count += 1
        start = start +1 


print(count)

#시간초과코드 
#for i in range(len(num_list)-1) : 
    
#    for j in range(i+1 , len(num_list)) : 
            
#        if num_list[i] + num_list[j] == x :
#            count += 1
#            break 
        

            