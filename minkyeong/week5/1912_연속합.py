#연속된 몇개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합 
#1. 연속된 수들의 누적합 계산
#2. 만일 누적합이 음수가 될 경우 0으로 업데이트 
#3. 누적합이 지금까지의 최대합보다 커질 경우 최대합으로 업데이트 

n = int(input())
num_list = list(map(int,input().split())) 

curr_num , max_num = 0 , -1001 

for i in range(n) : 

	curr_num += num_list[i] # 누적합 구하기 (연속된 숫자의 합을 구해야하므로)  
	
	if curr_num > max_num : #만일 누적합이 지금까지 최대합보다 크다면 
		max_num = curr_num    #누적합을 최대합으로 업데이트
	
	if curr_num < 0 : #만일 누적합이 음수가 될 경우, 0으로 업데이트
		curr_num = 0 

print(max_num) 