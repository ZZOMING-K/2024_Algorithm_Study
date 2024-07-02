def solution(word):
    answer = 0
    
    word_dict = {'A' : 0, 'E' : 1, 'I' : 2, 'O' : 3, 'U' : 4}
    
    value_list = [1]
    for i in range(1, len(word_dict)):
        value_list.append(len(word_dict) ** i + value_list[-1])
    value_list = value_list[::-1]
    
    for idx, w in enumerate(word):
        answer += value_list[idx] * word_dict[w] + 1
    
    return answer