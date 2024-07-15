def solution(word):
    vowel = ['X', 'A', 'E', 'I', 'O', 'U']
    target = 0
    for i in range (len(word)):
        for j in range(6):
            if word[i] == vowel[j]:
                target = target + (j * (10 ** (len(word)-1 - i)))
    
    num = 1
    answer = 1
    
    while num != target:
        answer = answer + 1
        if num // 10000 == 0:
            num = num * 10 + 1
            continue
        else:
            if num % 10 != 5:
                num = num + 1
                continue
            else:
                while num % 10 == 5:
                    num = num // 10
                num = num + 1
                continue
    return answer
