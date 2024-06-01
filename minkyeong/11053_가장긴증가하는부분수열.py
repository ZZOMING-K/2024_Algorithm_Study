A = int(input()) #수열의 크기 입력 
A_list = list(map(int,input().split())) #수열A를 이루고 있는 숫자들  

dp = [1] * A 

for i in range(A) :
	for j in range(i) : 
		if A_list[i] > A_list[j] : #현재 위치 원소보다 이전 위치에 있는 원소가 작은 경우  
			dp[i] = max(dp[i] , dp[j] + 1) #이전 위치에 있는 숫자 중 최대 DP 값 + 1 을 해준다. 
 
print(max(dp)) 



#런타임에러 코드 (RunTime Error Code) 

# A = int(input()) #수열의 크기 입력 
# A_list = list(map(int,input().split())) #수열A를 이루고 있는 숫자들 

# curr_num = A_list[0] #첫번째 숫자 
# result = 1

# for i in range(1,A+1) :
# 	if A_list[i] > curr_num : #만일 탐색하는 숫자가 현재까지 가장 큰 숫자보다 크다면 갱신 
# 		curr_num = A_list[i]
# 		result += 1             #result += 1 
		 
# print(result) 	