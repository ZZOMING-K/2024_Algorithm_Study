from collections import defaultdict

def solution(genres, plays):
    answer = []
    
    idx_lst = [i for i in range(len(plays))]
    song_lst = [[gen, play, i] for gen, play, i in zip(genres, plays, idx_lst)]

    song_dict = defaultdict(int)
    for gen, play in zip(genres, plays):
        song_dict[gen] += play
    
    song_lst.sort(reverse = True, key = lambda x : (song_dict[x[0]], x[1]))
    
    song_count = defaultdict(int)
    for song in song_lst:
        if song_count[song[0]] < 2:
            song_count[song[0]] += 1
            answer.append(song[2])
    
    return answer