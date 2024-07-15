from collections import deque

def solution(progresses, speeds):
    answer = []
    
    progress_q = deque(progresses)
    speed_q = deque(speeds)
    day = 1
    count = 0

    while progress_q:
        current_progress = progress_q[0]
        current_speed = speed_q[0]
        
        if current_progress + (current_speed * day) >= 100:
            progress_q.popleft()
            speed_q.popleft()
            count += 1

            if not progress_q:
                answer.append(count)

            elif progress_q:
                if progress_q[0] + (speed_q[0] * day) < 100:
                    answer.append(count)    
                    
        elif current_progress + (current_speed * day) < 100:
            day += 1
            count = 0

    return answer