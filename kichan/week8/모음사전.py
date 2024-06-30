from itertools import product

def solution(word):
    moum = ['A', 'E', 'I', 'O', 'U']
    arr = []
    
    for i in range(1, 6):
        for comb in product(moum, repeat=i):
            arr.append(''.join(comb))
    
    arr = sorted(arr)
    
    return arr.index(word)+1