def solution(name):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    answer = 0
    n = len(name)
    move = n - 1

    for i in range(n):
       
        current_idx = alphabet.index(name[i])
        answer += min(current_idx, 26 - current_idx)

       
        next_index = i + 1
        while next_index < n and name[next_index] == 'A':
            next_index += 1
        
        
        move = min(move, i + n - next_index + min(i, n - next_index))

    answer += move
    return answer


