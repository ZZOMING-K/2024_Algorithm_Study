N = int(input()) #사람 수 
P_list = list(map(int,input().split())) #i번 사람이 돈을 인출하는데 걸리는 시간  

#오름차순으로 정렬 
P_list = sorted(P_list) 

time = 0 #i번 사람이 줄을 서서 돈을 인출하는데 걸리는 시간 
sum_time = 0 #각 사람이 돈을 인출하는데 필요한 시간의 합 

for p in P_list : 
    time += p # i번째 사람이 줄을 서서 돈을 인출하는데 걸리는 시간 
    sum_time += time #누적합을 계산하기 위해 더하기 

print(sum_time)