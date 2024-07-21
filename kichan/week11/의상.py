def solution(clothes):
    answer = 1
    
    cloth_dic = dict()
    for item,category in clothes:
        if category in cloth_dic:
            cloth_dic[category].append(item)
        else:
            cloth_dic[category] = [item]
            
    for category in cloth_dic:
        answer *= (len(cloth_dic[category])+1)
    
    answer -=1
    
    return answer