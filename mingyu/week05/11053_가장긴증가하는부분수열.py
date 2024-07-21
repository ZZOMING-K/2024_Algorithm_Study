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
