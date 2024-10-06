def solution(n, stations, w):
    answer = 0
    start = 1 # 첫번째 아파트
    wifi_range = 2 * w + 1 # 기지국 하나가 커버할 수 있는 범위
    
    for station in stations:
        front_range = station - w - start # 기지국 기준으로 앞쪽에 커버 못하는 영역의 길이
        if front_range > 0:
            if front_range % wifi_range == 0: # 커버 못하는 영역의 길이가 기지국의 범위로 나누어 떨어지면 그 몫만큼 설치
                answer += (front_range // wifi_range)
            else: # 커버 못하는 영역의 길이가 기지국의 범위로 나누어 떨어지지 않으면 그 몫에다가 +1을 더해준 만큼 설치
                answer += (front_range // wifi_range) + 1
        
        start = station + w + 1  # 먼저 설치된 기지국 기준으로 뒷쪽으로 커버할 수 있는 범위 밖부터 다시 체크

    # stations의 마지막 기지국 기준으로 뒷쪽에 커버하지 못하는 영역이 있는지 확인    
    back_range = n - start + 1
    if back_range > 0: # 커버하지 못하는 영역이 있다면
        if back_range % wifi_range == 0: # 기지국의 범위로 나누었을 때 나누어 떨어지면 그 몫만큼 설치
            answer += (back_range // wifi_range)
        else: # 기지국의 범위로 나누었을 때 나누어 떨어지지 않으면 그 몫에다가 +1을 더해준 만큼 설치
            answer += (back_range // wifi_range) + 1
        
    return answer