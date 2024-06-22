n = int(input())
num_list = list(map(int,input().split()))

num_list.sort(reverse = True) #내림차순 정렬 

#3개 곱할 때의 경우 
#양수*양수*양수 
#음수*음수*양수 

max3_1 = num_list[0] * num_list[1] * num_list[2]
max3_2 = num_list[-1] * num_list[-2] * num_list[0] 
max3 = max(max3_1 , max3_2)

#2개 곱할 때의 경우 
#양수*양수
#음수*음수 

max2_1 = num_list[0] * num_list[1]
max2_2 = num_list[-1] * num_list[-2] 
max2 = max(max2_1 , max2_2)

print(max(max3 , max2))

#음수*음수를 고려안한 코드 
# answer = 1
# count = 0
# for num in num_list :
#     if num > 1 :
#         answer *= num 
#         count += 1 
#         if count == 3 :
#             break 
#     else :
#         break

# print(answer)