def solution(tickets):
    
    #리스트 정렬 
    tickets = sorted(tickets , key = lambda x : (x[0] , x[1]))
    visited = [False] * len(tickets)
    answer = ["ICN"]
    
    def dfs(start_v) :
        for i in range(len(tickets)) :
            if tickets[i][0] == start_v and not visited[i]:
                answer.append(tickets[i][1])
                visited[i] = True 
                dfs(tickets[i][1])
    dfs("ICN")
    return answer