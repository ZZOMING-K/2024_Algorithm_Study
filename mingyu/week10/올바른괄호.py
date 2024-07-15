def solution(s):
    s = list(s)
    exitbracket = 0
    while s:
        now = s.pop()
        if now == ')':
            exitbracket = exitbracket + 1
        else:
            exitbracket = exitbracket - 1
            if exitbracket < 0:
                return False
    
    if exitbracket == 0:
        return True
    else:
        return False
