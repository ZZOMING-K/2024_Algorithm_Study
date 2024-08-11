def solution(phone_book):
    answer = True
    phone_book.sort(key = lambda x: len(x), reverse = True)
    judgement = {}
    for i, number in enumerate(phone_book):
        if judgement.pop(number, 0) == 1:
            answer = False
            break
        else:
            for j in range(len(number)):
                judgement[number[:j+1]] = 1
    return answer
