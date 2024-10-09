def solution(dirs):
    answer = 0
    
    # 상하좌우 이동하는 경우
    U = [0, 1]
    D = [0 , -1]
    L = [-1, 0]
    R = [1, 0]
    
    current_loc = [0, 0] # 현재 위치(시작 위치 : x, y)
    total_path = [] # 지나가본 길을 담는 리스트
    
    for s in dirs:
        if s == 'U':
            if current_loc[1] == 5: # 현재 y 좌표가 5라면 더 이상 위로 이동할 수 없음
                continue
            next_loc = [a + b for a, b in zip(current_loc, U)] # 현재 위치에서 다음에 이동할 위치
            path = (current_loc, next_loc) # 이동한 길
            reverse_path = (next_loc, current_loc) # 이동한 길의 역방향
            current_loc = next_loc # 이동하고 난 뒤의 현재 위치
            if path not in total_path and reverse_path not in total_path: # 이동한 길과 그 역방향까지 모두 total_path에 없다면 처음 가본 길
                total_path.append(path)
                answer += 1
            else:
                continue
        elif s == 'D':
            if current_loc[1] == -5:
                continue
            next_loc = [a + b for a, b in zip(current_loc, D)]
            path = (current_loc, next_loc)
            reverse_path = (next_loc, current_loc)
            current_loc = next_loc
            if path not in total_path and reverse_path not in total_path:
                total_path.append(path)
                answer += 1
            else:
                continue
        elif s == 'L':
            if current_loc[0] == -5:
                continue
            next_loc = [a + b for a, b in zip(current_loc, L)]
            path = (current_loc, next_loc)
            reverse_path = (next_loc, current_loc)
            current_loc = next_loc
            if path not in total_path and reverse_path not in total_path:
                total_path.append(path)
                answer += 1
            else:
                continue
        elif s == 'R':
            if current_loc[0] == 5:
                continue
            next_loc = [a + b for a, b in zip(current_loc, R)]
            path = (current_loc, next_loc)
            reverse_path = (next_loc, current_loc)
            current_loc = next_loc
            if path not in total_path and reverse_path not in total_path:
                total_path.append(path)
                answer += 1
            else:
                continue

            
    return answer