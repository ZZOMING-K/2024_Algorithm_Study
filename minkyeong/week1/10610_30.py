# 30의 배수 -> 10의 배수이자 3의 배수 
# 10의 배수는 0으로 끝나야 하며, 3의 배수는 각 자리 수의 합이 3의 배수여야 함. 

N = input()

#내림차순으로 정렬 
N = sorted(N , reverse = True)

num_sum = sum([int(i) for i in N])

#만일 각 자리 수의 합이 3으로 나누어 떨어지지 않거나, 0이 포함되지 않는다면 -1 반환 
if (num_sum % 3 != 0) or ('0' not in N ):
    result = -1
else :
    result = "".join(N) #아닐경우 join을 활용하여 문자열을 합친뒤 출력 

print(result)      