def solution(participant, completion):
    answer = ''
    
    participant.sort()
    completion.sort()
    
    for name1, name2 in zip(participant[:-1], completion):
        if name1 != name2:
            answer = name1
            break
            
    if answer == '':
        answer = participant[-1]
            
    return answer