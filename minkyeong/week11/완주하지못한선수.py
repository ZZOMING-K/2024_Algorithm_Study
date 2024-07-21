from collections import Counter
def solution(participant, completion) :
    participant , completion = Counter(participant) , Counter(completion)
    answer = participant - completion
    return list(answer.keys())[0]