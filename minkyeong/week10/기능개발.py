def solution(progresses, speeds):
    
    day_list = []
    
    for i in range(len(speeds)) : 
        # 100% 달성하기 까지 걸리는기간 리스트 생성 
        if (100 - progresses[i]) % speeds[i] == 0 : 
            day_list.append((100 - progresses[i]) // speeds[i])
        else : 
            day_list.append(((100 - progresses[i]) // speeds[i]) +1)
    
    count = 1
    result = []
    max_day = day_list[0] 
    
    for j in range(1,len(day_list)) : 
        if day_list[j] <= max_day : 
            count+= 1 
        else :
            result.append(count)
            count = 1 #count 초기화 
            max_day = max(max_day , day_list[j])
            #time += 1 #time 넘기기 
    result.append(count)
    
    return result 