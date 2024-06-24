#주어지는 수의 개수 
N = int(input()) 
#주어지는 수 
num_list = list(map(int,input().split())) 
#주어지는 연산자의 수 (덧셈 ,뺄셈, 곱하기 ,나누기 순) 
calcum = list(map(int, input().split())) 
max_num , min_num = float('-inf') , float('inf') 


def recur(number , res , add,  sub,  mul,  div) : 
	global max_num , min_num 
	if number >=N :
		max_num = max(max_num , res) 
		min_num = min(min_num , res)  

	if add > 0 :
		recur(number+1, res + num_list[number] , add-1 , sub , mul , div) 
	if sub > 0 :
		recur(number+1,  res - num_list[number] , add , sub-1 , mul , div)
	if mul > 0 :
		recur(number+1,   res * num_list[number] , add , sub , mul -1 , div) 
	if div > 0 :
		recur(number+1 ,  res / num_list[number] , add, sub , mul , div-1) 

recur(1 , num_list[0] , calcum[0] , calcum[1] , calcum[2] , calcum[3]) 
print(max_num)
print(min_num)   