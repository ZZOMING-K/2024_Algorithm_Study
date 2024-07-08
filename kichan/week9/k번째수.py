def solution(array, commands):
    answer = []
    
    for i in range(len(commands)):
        start = commands[i][0] -1
        end = commands[i][1]
        new_arr = sorted(array[start:end])
        answer.append(new_arr[commands[i][2]-1])
    
    return answer