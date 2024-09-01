def solution(number, k):
    answer = ''
    temp = []
    for i, num in enumerate(number):
        if k == 0:
            for j in range(i, len(number)):
                temp.append(number[j])
            break
        if i != len(number) - 1 and number[i] < number[i + 1]:
            k = k - 1
            while k > 0 and temp:
                now = temp.pop()
                if now < number[i + 1]:
                    k = k - 1
                else:
                    temp.append(now)
                    break
            continue
        else:
            temp.append(num)
    for i in temp:
        answer = answer + i
    while k > 0:
        k = k - 1
        answer = answer[:-1]
    return answer
