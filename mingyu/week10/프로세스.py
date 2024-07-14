def solution(priorities, location):
    answer = 1
    while priorities:
        if priorities[0] == max(priorities):
            if location == 0:
                return answer
            else:
                location = location - 1
                priorities = priorities[1:]
                answer = answer + 1
        else:
            location = location - 1
            if location == -1:
                location = len(priorities) - 1
            priorities.append(priorities[0])
            priorities = priorities[1:]
                
