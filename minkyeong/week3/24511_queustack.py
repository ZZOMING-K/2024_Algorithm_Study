from collections import deque
import sys
input = sys.stdin.readline

N = int(input()) #큐스택을 구성하는 자료구조의 개수 
dst_list = list(map(int,input().split())) #자료구조 입력받기
dst_data = list(map(int,input().split())) #데이터 입력받기
M = int(input())
C = list(map(int,input().split())) #삽입할 원소 C 


q = deque()

for idx , d in enumerate(dst_list):
    if d == 0 : #만일 큐라면 원소 추가 
        q.append(dst_data[idx])


for c in C :
    q.appendleft(c) 
    x = q.pop() 
    print(x , end = " ")               
    


# from collections import deque
# import sys
# input = sys.stdin.readline

# N = int(input()) #큐스택을 구성하는 자료구조의 개수 
# dst_list = list(map(int,input().split())) #자료구조 입력받기
# dst_data = list(map(int,input().split())) #데이터 입력받기
# M = int(input())
# C = list(map(int,input().split())) #삽입할 원소 C 

# dst = []

# for i in range(N):
#     if dst_list[i] == 0 : #만일 큐라면  
#         dst.append(deque([dst_data[i]]))
#     else:
#         stack = [(dst_data[i])]
#         dst.append(stack)
        

# #만일 자료구조가 스택이라면 pop, 아니라면 popleft 

# for c in C : 
    
#     dst[0].append(c) #수열원소 추가 
    
    
#     for i in range(N-1) : 
    
#         if  dst_list[i] == 1 :  
#             x = dst[i].pop()
#             dst[i+1].append(x)
#         else :
#             x = dst[i].popleft()
#             dst[i+1].append(x)
            
    
#     if dst_list[-1] == 1 :
#         x = dst[-1].pop()
#         print(x , end = " ")
#     else :
#         x =dst[-1].popleft()
#         print(x , end = " ")
        


    
