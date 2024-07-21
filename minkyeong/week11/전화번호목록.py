def solution(phone_book):
    numbers = {}
    for phone in phone_book :
        numbers[phone] = 1 
    
    for nums in phone_book :
        prefix = ""
        for num in nums :
            prefix+=num
            if prefix in numbers and prefix != nums :
                return False 
                break 
    return True 