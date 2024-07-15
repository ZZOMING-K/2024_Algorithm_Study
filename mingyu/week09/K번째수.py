def solution(array, commands):
    answer = []
    while commands:
        command = commands[0]
        if commands:
            commands = commands[1:]
        copied = array[command[0] - 1:command[1]]
        copied.sort()
        answer.append(copied[command[2] - 1])
    return answer
