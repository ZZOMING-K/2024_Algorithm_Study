def solution(answers):
    case1 = [1, 2, 3, 4, 5]
    case2 = [2, 1, 2, 3, 2, 4, 2, 5]
    case3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    answer = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == case1[i%5]:
            answer[0] = answer[0] + 1
        if answers[i] == case2[i%8]:
            answer[1] = answer[1] + 1
        if answers[i] == case3[i%10]:
            answer[2] = answer[2] + 1
    
    score = max(answer)
    returnarr = []
    for i in range(3):
        if answer[i] == score:
            returnarr.append(i+1)
    return returnarr
            
