def solution(genres, plays):
    answer = []
    matching = {}
    groupbygenres = {}
    populersong = {}
    for i, genre in enumerate(genres):

        if matching.get(genre, 0) == 0:
            matching[genre] = len(list(matching.keys())) + 1
        genre = matching[genre]
        
        groupbygenres[genre] = groupbygenres.get(genre, 0) + plays[i]
        if populersong.get(genre, 0) == 0:
            populersong[genre] = [[plays[i], i]]
        else:
            populersong[genre].append([plays[i], i])
    sortingGen = []
    for i in groupbygenres.keys():
        sortingGen.append([groupbygenres[i], i])
    sortingGen.sort()
    #print(matching)
    #print(sortingGen)
    #print(groupbygenres)
    #print(populersong)
    #print()
    while sortingGen:
        now = sortingGen.pop()[1]
        populersong[now].sort(key = lambda x : (x[0], -1 * x[1]))
        
        for i in range(2):
            if populersong[now]:
                answer.append(populersong[now].pop()[1])
        #print(populersong)
    
    return answer
