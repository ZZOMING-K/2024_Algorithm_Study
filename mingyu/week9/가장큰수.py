def solution(numbers):
    strnumbers = []
    for number in numbers:
        strnumbers.append(str(number))
    strnumbers.sort(key=lambda x : int(x[0]))
    #print(strnumbers)
    answer = ""
    
    while strnumbers:
        answerlist = [strnumbers.pop()]
        while strnumbers and strnumbers[-1][0] == answerlist[0][0]:
            answerlist.append(strnumbers.pop())

        beforesort = []
        #print(answerlist)
        for i in range(len(answerlist)):
            intvalue = int(answerlist[i])
            strvalue = answerlist[i]
            
            for i in range(4 - len(strvalue)):
                intvalue = intvalue * 10 + int(strvalue[0])
                           
            beforesort.append([intvalue, strvalue])
            #print(beforesort[-1])
        #print(beforesort)
        aftersort = sorted(beforesort)
        #print(aftersort)
        while aftersort:
            detailsort = [aftersort.pop()]
            while aftersort and aftersort[-1][0] == detailsort[0][0]:
                detailsort.append(aftersort.pop())
                
            for i in range(len(detailsort)):
                detailsort[i][0] = ''
                for j in range(1, 5): #1 -> -1, 2 -> -2, 3 -> -3, 4 -> -4
                    if len(detailsort[i][1]) >= j:
                        detailsort[i][0] = detailsort[i][0] + list(detailsort[i][1])[-1 * j]
                    else:
                        detailsort[i][0] = detailsort[i][0] + '0'
                detailsort[i][0] = int(detailsort[i][0])
            #print(detailsort)
            detailsort.sort()
            #print(detailsort)
            while detailsort:
                answer = answer + detailsort.pop()[1]

    #print(answer)
    return '0' if answer[0] == '0' else answer
