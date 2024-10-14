def solution(s):
    answer = []
    
    total_0 = 0
    number_convert = 0
    
    while s != '1':
        count_0 = s.count('0') # s 문자열에 있는 '0'의 개수
        total_0 += count_0
        c = len(s) - count_0 # c = 문자열 s의 길이 - 0의 개수
        s = str(bin(c)[2:]) # c를 이진수로 변환
        number_convert += 1
        
    answer = [number_convert, total_0]    
    return answer