import sys 

T = int(sys.stdin.readline()) 

arr = [0,1,1,1] #1~3번째 나선에 있는 정삼각형의 변의 길이 

for i in range(4,100+1) : #N은 최대 100이므로 100개의 정삼각형 변의 길이 배열 생성 
	arr.append(arr[i-3] + arr[i-2]) 

for _ in range(T) :
	n = int(input()) 
	print(arr[n])  #저장해둔 변의 길이를 바로 찾기 
 

#런타임에러 발생
#For문 돌릴때 마다 배열을 새로 생성해서 오래 걸리는 건가요?  
# T = int(input()) 

# for _ in range(T) : 
	
# 	N = int(input()) 

# 	P = [0 for _ in range(N+1)] 
# 	P[1] , P[2] , P[3]  = 1 ,1 ,1 

# 	for i in range(3 , N+1) :
# 		P[i] = P[i-3] + P[i-2] 

# 	print(P[N])    