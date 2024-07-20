def solution(participant, completion):
    
    p_dict = {}

    for p in participant:
        if p in p_dict:
            p_dict[p] += 1
        else:
            p_dict[p] = 1
    
    for c in completion:
        if c in p_dict:
            p_dict[c] -= 1
            if p_dict[c] == 0:
                del p_dict[c]
    
    for key in p_dict:
        return key