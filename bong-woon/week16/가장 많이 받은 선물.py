def solution(friends, gifts):
    answer = [0] * len(friends)
    table = [[0] * len(friends) for _ in range(len(friends))]
    
    gift_index = [0] * len(friends)
    
    for gift in gifts:
        give, receive = gift.split()
        give_idx, receive_idx = friends.index(give), friends.index(receive)
        gift_index[give_idx] += 1
        gift_index[receive_idx] -= 1
        table[give_idx][receive_idx] += 1
                        
    for i in range(len(friends)):
        for j in range(i + 1, len(friends)):
            if table[i][j] > table[j][i]:
                answer[i] += 1
            elif table[i][j] < table[j][i]: 
                answer[j] += 1
            else:
                if gift_index[i] > gift_index[j]:
                    answer[i] += 1
                elif gift_index[i] < gift_index[j]:
                    answer[j] += 1

    return max(answer)