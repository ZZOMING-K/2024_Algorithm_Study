def solution(number , k ) : 
    
    stack = []
    for num in number :
        while k > 0  and stack and stack[-1] < num :
            stack.pop()
            k -= 1 
        stack.append(num) 
    
    if k > 0 : #만일 k가 남아있다면 (숫자가 내림차순으로 pop를 실행하지 않은 경우) 
        stack = stack[:-k]
    return ''.join(stack)


