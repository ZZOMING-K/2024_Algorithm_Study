def solution(tickets):
    answer = []
    dictionary = {}
    for ticket in tickets:
        source = ticket[0]
        destination = ticket[1]
        if dictionary.get(source, 0) == 0:
            dictionary[source] = [destination]
        else:
            dictionary[source].append(destination)

    #print(dictionary)
    #print()
    nextArr = [["ICN"]]
    
    for i in range(len(tickets)):
        nowArr = nextArr
        nextArr = []
        #print(i, nowArr)
        for j, now in enumerate(nowArr):
            last = now[-1]
            tmp = dictionary.get(last, [])[:]
            for k, n in enumerate(now):
                if k < len(now) - 1 and n == last:
                    tmp.remove(now[k + 1])
            #print(tmp)
            for k, country in enumerate(dictionary.get(last, [])):
                if country in tmp:
                    #print(f"now: {now}, country: {country}")
                    tmp2 = now[:]
                    tmp2.append(country)
                    nextArr.append(tmp2)
    #print(nextArr)
    final = []
    for i in nextArr:
        final.append(' '.join(i))
    #print(final)
    final.sort()
    #print(final)
    return final[0].split(' ')
