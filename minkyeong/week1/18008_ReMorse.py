from collections import Counter

s = input()
# 알파벳인지 확인 및 공백제거, 대문자 변환
filter_s ="".join([char.upper() for char in s if char.isalpha()])  

# 문자별 빈도 수 내림차순
cnt_word = sorted(list(Counter(filter_s).values()), reverse=True)

#모스부호 배열 길이 리스트 생성 (오름차순) 
#모스부호 배열의 길이 =>  1부터 2씩 증가
#해당 길이를 생성할 수 있는 모스부호 배열 조합의 개수 => 피보나치 수열 

current_num = 1
f1, f2 = 1, 2
result = []

n = len(cnt_word)

while len(result) < n:
    result.extend([current_num] * f1) #현재 피보나치 수만큼 길이 추가 
    current_num += 2 # 길이 업데이트 
    f1, f2 = f2, f1 + f2  # 피보나치 수 업데이트

result = result[:n]

# 총 문자길이 = (문자별 빈도수 X 모스부호 배열 길이) + 문자간 공백 길이
total_length = sum([a * b for a, b in zip(cnt_word, result)]) + (len(filter_s) - 1) * 3
print(total_length)