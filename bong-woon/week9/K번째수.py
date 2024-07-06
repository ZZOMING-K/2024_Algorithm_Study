def solution(array, commands):
    answer = []
    
    for command in commands:
        split_array = array[command[0]-1:command[1]]
        split_array.sort()
        num = split_array[command[2]-1]
        answer.append(num)
        
    return answer