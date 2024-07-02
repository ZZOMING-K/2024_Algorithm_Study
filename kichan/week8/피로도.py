from itertools import permutations

def solution(k, dungeons):
    answer = []
    
    dungeons = list(permutations(dungeons, len(dungeons)))
    
    for dungeon in dungeons:
        cnt = 0
        full_hp = k
        for info in dungeon:
            hp = info[0]
            cost = info[1]

            if full_hp>=hp:
                full_hp-=cost
                cnt += 1

        answer.append(cnt)
        
    return max(answer)