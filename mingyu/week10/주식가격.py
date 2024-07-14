def solution(prices):
    answer = []
    increase = []
    for i, price in enumerate(prices):
        answer.append(0)
        increase.append(i)
        for j in range(i):
            if j in increase:
                answer[j] = answer[j] + 1
            if j in increase and prices[j] > price:
                increase.remove(j)
        #print(price)
        #print(increase)
        #print(answer)
    return answer


prices = [10, 9, 8, 7, 6, 5, 4]

print(solution(prices))
