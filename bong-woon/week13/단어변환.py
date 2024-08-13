from collections import deque, defaultdict
def solution(begin, target, words):
    answer = 0
    
    graph = defaultdict(list)
    words.append(begin)
    
    def compare_word(word1, word2):
        count = 0
        for i in range(len(begin)):
            if word1[i] != word2[i]:
                count += 1
        
        if count == 1:
            return True
        else:
            return False
    
    for i in range(len(words)-1):
        for j in range(i + 1, len(words)):
            if compare_word(words[i], words[j]) == True:
                graph[words[i]] += [words[j]]
                graph[words[j]] += [words[i]]
                
    visited = {}
    
    def bfs(start, graph):
        q = deque()
        q.append((start, 0))
        visited[start] = True
        
        while q:
            current_word, current_count = q.popleft()
            
            if current_word == target:
                return current_count
            
            for next_word in graph[current_word]:
                if next_word not in visited:
                    q.append((next_word, current_count + 1))
                    visited[next_word] = True     
        return 0
                        
    answer = bfs(begin, graph)
                    
    return answer