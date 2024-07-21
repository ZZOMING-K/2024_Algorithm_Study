from collections import defaultdict, Counter

def solution(genres, plays):     
    answer = defaultdict(list)
    song = defaultdict(int)
    
    for i in range(len(plays)) :
        answer[genres[i]].append((i,plays[i])) #장르별 인덱스와 재생횟수 추가 
        song[genres[i]] += plays[i] #장르별 총 재생횟수 계산 
        
    #장르별로 내림차순 정렬 
    song = sorted(song.keys() , key = lambda x : song[x] , reverse = True)
    
    result = []
    #장르 내에서 재생 횟수 순 내림차순 , 같을 경우 고유 번호 순 오름차순 정렬 
    for s in song :
        res = sorted(answer[s], key = lambda x : (-x[1] , x[0]))
        result.extend(res[:2]) #장르당 최대 2곡씩 추천하므로 0,1까지 슬라이싱
    
    answer = [idx for idx, value in result] #index만 추출해서 return 하기 
    return answer