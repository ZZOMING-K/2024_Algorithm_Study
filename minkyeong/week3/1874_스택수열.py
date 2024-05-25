import sys
N = int(sys.stdin.readline()) 
num_list = list(int(sys.stdin.readline())  for _ in range(N))

new_stack  , result  , answer = [] , [] , True

i = 1

for num in num_list :  
    
    while i <= num :  
        new_stack.append(i)
        result.append('+')
        i += 1 
    
    if new_stack[-1] == num : #만일 stack 마지막 원소가 pop 진행 후 '-' 추가 
        new_stack.pop()
        result.append('-') 
    
    else : #만일 수열을 만들 수 없는 경우 False로 설정 
        answer = False
        break

if not answer :
    print("NO") 
else :               
    print(*result , sep = '\n')
            
     
