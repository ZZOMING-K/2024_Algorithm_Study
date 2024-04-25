N , x = map(int,input().split())
A = list(map(int,input().split())) 

for i in A : #리스트(A) 에서 각 요소(i)를 꺼낸다. 
    if i < x :  #만일 i가 x보다 작다면 출력 
        print(i , end = " ") #end= " "을 사용하여 공백으로 다음 출력과 분리될 수 있도록 한다. 