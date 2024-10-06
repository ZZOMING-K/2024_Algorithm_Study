def solution(skill, skill_trees):
    answer = 0
    
    for st in skill_trees: 
        sk_tree = ''
        for s in st: # 유저들이 만든 스킬트리에서
            if s in skill: # 스킬이 skill에 포함되어 있다면 sk_tree에 추가
                sk_tree += s
                
        if sk_tree == skill[:len(sk_tree)]: # 만들어진 sk_tree가 주어진 선행 스킬트리와 같다면 가능한 스킬트리
            answer += 1
    
    return answer