def solution(genres, plays):
    answer = []
    play = dict()
    play_idx = dict()
    
    for i in range(len(genres)):
        play[genres[i]] = play.get(genres[i],0) + plays[i]
        
        if genres[i] in play_idx:
            play_idx[genres[i]].append((plays[i], i))
        else:
            play_idx[genres[i]] = [(plays[i], i)]
            
    sorted_genre = sorted(play.keys(), key = lambda x:play[x], reverse=True) 
    
    for genre in sorted_genre:
        songs = sorted(play_idx[genre], key=lambda x: (-x[0], x[1]))
        for s in songs[:2]:
            answer.append(s[1])

    return answer