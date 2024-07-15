def solution(s):
    answer = True
    
    lst = []

    for char in s:
        if char == '(':
            lst.append(char)
        elif char == ')':
            if len(lst) == 0:
                answer = False
                return answer
            else:
                lst.pop()
        
    if len(lst) == 0:
        answer = True
    else:
        answer = False

    return answer