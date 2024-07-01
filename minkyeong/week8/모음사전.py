from itertools import product 

def solution(word): 
    
    vowel = ['A','E','I','O','U']
    arr = []
    
    for i in range(1,6) :
        for p in product(vowel , repeat = i) :
            arr.append(''.join(p))
        
    arr.sort() #오름차순 정렬 
    
    for i in range(len(arr)) : 
        if arr[i] == word :
            answer = i+1 
            break 
        
    return answer