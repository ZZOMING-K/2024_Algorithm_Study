def solution(phone_book):
    answer = True
    phone_book.sort(key = lambda x: len(x), reverse = True)
    print(phone_book)
    return answer
