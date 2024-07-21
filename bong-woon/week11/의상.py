from collections import defaultdict

def solution(clothes):
    answer = 1
    
    clothes_dict = defaultdict(int)
    
    for cloth in clothes:
        clothes_dict[cloth[1]] += 1
        
    if len(list(clothes_dict.keys())) == 1:
            answer = list(clothes_dict.values())[0]
    elif len(list(clothes_dict.keys())) >= 2:
        for count in clothes_dict.values():
            answer *= (count + 1)
        answer = answer - 1
            
    return answer