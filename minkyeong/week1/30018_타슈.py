N = int(input())  #대여소 개수 
a_list = list(map(int,input().split()))  
b_list = list(map(int,input().split()))

count = 0

#만일 a보다 b에 자전거가 더 적다면, 부족한 수만큼 a로 옮겨야 한다. 
for i in range(len(a_list)) :  
    if a_list[i] > b_list[i] : 
        count+= a_list[i] - b_list[i]

print(count)