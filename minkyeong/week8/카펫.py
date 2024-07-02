def solution(brown, yellow):
    answer = [0,0]
    
    # 카펫의 가로길이는 세로 길이와 같거나 세로길이보다 길다. 
    # 아래 조건에 해당하는 수를 찾는다. 
    # w * h = brown + yellow , 2w + 2h - 4 = brown , w >= h  

    for w in range(3, 2500) : 
        for h in range(3 , 2500) : 
            if ((w * h) == (brown + yellow)) and ((w + h) == (brown + 4) / 2) and (w>=h):
                    answer[0] , answer[1] = w,h 
                    break
    return answer

    #for 반복문 범위를 어떻게 설정하지 고민하는데 시간이 조금 걸림 
    # w+h = (brown + 4)/2 인데 brown이 최대 5000이므로 (5000+4)/2하면 2502이다. 
    # 여기서 brown과 yellow는 각각 8이상 1이상이므로, w와 h는 아무리 작아도 3,3 이다.
    # 따라서 w와 h 범위를 3부터 (2502-3)=2499로 설정