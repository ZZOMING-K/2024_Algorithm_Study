def solution(n, words):
    
    used = []
    used.append(words[0])
    last_word = words[0][-1]
    
    turn = 1
    player = 1
    
    for i in range(1, len(words)):
        
        
        player += 1
        
        if player > n:
            turn += 1
            player = 1
        
        if (words[i] not in used) and (words[i][0] == last_word):
            used.append(words[i])
            last_word = words[i][-1]
        
        else:
            return [player, turn]
        
    else:
        return [0,0]