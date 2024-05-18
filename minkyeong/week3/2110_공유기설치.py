N , C = map(int,input().split()) # 집 개수와 공유기 개수 입력받기 

wifi_list = [int(input()) for _ in range(N)]
wifi_list.sort() #오름차순 정렬 

min_len = 1 
max_len = wifi_list[-1] - wifi_list[0]


def place(distance) :
    count = 1 
    curr_num = wifi_list[0] #첫번째 공유기 위치  
    
    for i in range(1,N) :
        if wifi_list[i] - curr_num >= distance : #만일 설정된 거리보다 길다면 공유기 설치 
            count += 1 
            curr_num = wifi_list[i] #옮겨진 거리를 현재 공유기 위치로 설정 
            if count == C : #범위 내 공유기를 다 설치가능한 경우 True 반환 
                return True 
    
    return False  #

while min_len <= max_len : 
    mid = (min_len + max_len) // 2 #최대 길이를 이분탐색으로 찾기  
    
    if place(mid) : #범위 내 공유기를 설치한 경우 
        result = mid  #result에 저장 
        min_len = mid +1  
    else :
        max_len = mid -1

print(result)



#while min_len <= max_len :
    
#    mid = (min_len + max_len) // 2 #인접길이 설정 
    
#    i = wifi_list[0]
#    count = 1 
    
#    for c in range(C-1) : 
        
#        i_list = [num for num in wifi_list if num >= mid + i]

#        if i_list : #만일 리스트가 안빈다면 (범위를 넘어서지 않았다면) 
#            i = i_list[0]
#            count += 1 
            
#            if count == C :
#                result = mid 
#                min_len = mid+1 
#                break             
        
#        else : #범위를 벗어난다면 
#            max_len = mid-1 
#            break 
    
#print(result)
        