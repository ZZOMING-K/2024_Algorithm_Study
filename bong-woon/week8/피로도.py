from itertools import permutations

def solution(k, dungeons):
    answer = -1
    
    count_lst = []
    combs = permutations(dungeons, len(dungeons)) # 주어진 던전을 하나씩 방문할 모든 경우의 수
    
    for comb in combs: # ex) comb : ([80, 20], [50, 40], [30, 10])
        count = 0 # 방문한 던전 횟수
        current_k = k # 현재 피로도
        for dungeon in comb: # ex) dungeon : [80, 20]
            if dungeon[0] <= current_k:
                count += 1
                current_k -= dungeon[1]  
                
        count_lst.append(count)
        
    answer = max(count_lst)
                
    return answer