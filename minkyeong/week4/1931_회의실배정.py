import sys

n = int(input()) 

arr =[]

end_point , count = 0 , 0 

for i in range(n) :
    a , b = map(int,input().split())
    arr.append([a,b]) 

#회의가 끝나는 시간을  기준으로 정렬 후, 시작하는 시간을 기준으로 정렬 
arr.sort(key = lambda x : (x[1] , x[0]))

for new_start , new_end in arr : 
    if end_point <= new_start : #현재 끝나는 시간보다 시작하는 시간이 크거나 같다면 , 해당 회의 배정 
        count += 1 
        end_point = new_end 

print(count)