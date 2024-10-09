from collections import deque

def solution(skill, skill_trees):
    answer = 0
    
    for tree in skill_trees:
        skill_q = deque(skill)
        
        for t in tree:
            if t in skill_q:
                if t != skill_q.popleft():
                    break
        else:
            answer += 1        
    
    return answer