from collections import deque

def solution(priorities, location):
    answer = 0
    
    process_q = deque(priorities)
    index_q = deque([i for i in range(len(priorities))])
    
    while process_q:
        max_priority = max(process_q)
        first_process = process_q[0]
        
        if first_process >= max_priority:
            process_q.popleft()
            idx = index_q.popleft()
            answer += 1
            
            if idx == location:
                break
            else:
                continue
                
        elif first_process < max_priority:
            process_q.append(process_q.popleft())
            index_q.append(index_q.popleft())
            
    return answer