S = input() #0과 1로만 이루어진 문자열 받아오기 

#0과 1그룹 개수를 나타내는 dict 생성 
reverse_dict = {}

reverse_dict['0'] = S.count('01') #0인 그룹 count 세기 
reverse_dict['0'] = S.count('10') #1인 그룹 count 세기 
reverse_dict[S[-1]] += 1  #마지막 문자열로 어느 그룹인지 count 

print(min(reverse_dict.values())) #최소한의 뒤집기 -> 더 작은 그룹을 가진 수 만큼 뒤집기   