def solution(n, words):
    answer = []
    
    using_word = []
    using_word.append(words[0]) # 첫번째 단어는 무조건 사용 가능
    
    for i in range(1, len(words)):
        number = (i % n) + 1 # 사람들의 번호
        repeat = (i // n) + 1 # 반복한 횟수
        
        if words[i][0] == words[i - 1][-1] and words[i] not in using_word: # 사용된 단어가 아니고 앞의 단어의 마지막 글자와 현재 단어의 첫번째 글자가 같으면 끝말잇기는 성립
            using_word.append(words[i])
        else: # 끝말잇기가 성립되지 않으면 해당 번호와 반복 횟수를 리스트 형태로 반환
            answer = [number, repeat]
            return answer
    
    # for문을 돌면서 return 되지 않았다 = 끝말잇기는 끝까지 성립됐다
    answer = [0, 0]

    return answer