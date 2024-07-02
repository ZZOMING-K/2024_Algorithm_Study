from itertools import product

def solution(word):
    lst = ['A', 'E', 'I', 'O', 'U']
    word_lst = []
    answer = 0
    
    for i in range(1, len(lst) + 1):
        combs = product(lst, repeat = i)
        for comb in combs: # comb : (A, E, I, O, U)
            char = ''
            for s in comb:
                char += s
            word_lst.append(char)
    
    word_lst.sort()
    answer = word_lst.index(word) + 1
            
    return answer