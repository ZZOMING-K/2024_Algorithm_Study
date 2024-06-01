#필요한 정보 : 이전까지의 최대, 부분수열의 길이?
#길이별로 배열을 만들면 좋을듯?
#10 20 5 10 20 1 100 인 경우에서

#Answer배열 순서도 :
#10         -> 길이가 1일 때 최선은 10을 저장하는 것
#10 20      -> 2일때 최선은 20을 저장하는 것
#5 20      -> 길이가 1일 때 최선은 5를 저장하는 것
#5 10   -> 길이가 2일 때 최선은 10을 저장하는 것
#5 10 20 -> 길이가 3일 때 최선은 20을 저장하는 것
#5 10 20 100 -> 길이가 4일 때 최선은 100을 저장하는 것

N = int(input())
A = list(map(int, input().split()))

Answer = [A[0]]    #길이를 임의로 1 추가하였음

for i in A :
    #print(i)
    for j, value in enumerate(Answer):
        if value >= i:
            Answer[j] = i
            break
        else:
            continue
    if Answer[-1] < i:
        Answer.append(i)
    #print(Answer)
print(len(Answer))
