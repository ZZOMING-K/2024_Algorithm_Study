def solution(participants, completions):
    answer = ''
    player = {}
    for i, participant in enumerate(participants):
        player[participant] = player.get(participant, 0) + 1
    for i, completion in enumerate(completions):
        player[completion] = player[completion] - 1
        if player[completion] == 0:
            player.pop(completion, None)
    for i in player:
        answer = i
    return answer
