#소수 판별 : 제곱근까지만 하면 됨

def discrimination(target):
    root = target ** (1/2)
    root = int(root)
    for i in range(2, root + 1):
        if target % i == 0:
            return False
    return True

N = int(input())
answer = [2, 3, 5, 7]
for i in range(1, N):
    for j in range(len(answer)):
        answer[j] = answer[j] * 10

    decimal = []
    
    for j in answer:
        for k in range(10):
            if discrimination(j + k):
                decimal.append(j+k)
    answer = decimal
    
for i in answer:
    print(i)
            
