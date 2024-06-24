#편의상 I :1 , V : 2 , X : 3 , L : 4로 나타냄 
roma = { 1 : 1 , 2  : 5 , 3 : 10 , 4 : 50} 

N = int(input()) #사용할 수 있는 문자 개수 받아오기 
arr= [] 
sum_res = [] 

def recur(start , number) :
    
    if number == N :
        sum_res.append(sum(arr))
        return 
    
    for i in range(start , 5) :
        arr.append(roma[i])
        recur(number+1 , i)
        arr.pop()

arr = []
recur(1,0)
print(len(set(sum_res)))