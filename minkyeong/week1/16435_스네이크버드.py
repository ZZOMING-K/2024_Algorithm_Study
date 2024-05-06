#N(과일의 개수) 과 L(스네이크버드의 길이) 받아오기 
N ,L  = map(int,input().split()) 

h_list = list(map(int, input().split()))

#오름차순 정렬 
h_list = sorted(h_list)

#만일 스네이크 보다 과일의 높이가 낮거나 같으면 길이 +1 
for height in h_list :
    if height <= L :
        L = L+1 

print(L) #최종 스네이크버드 길이 출력 