def solution(begin, target, words):
    if begin in words:
        words.remove(begin)
    
    def similar(A, B):
        num = 0
        for i, a in enumerate(A):
            if a != B[i]:
                num = num + 1
        if num <= 1:
            return True
        else:
            return False
            
    answer = -1
    used = []
    nowArr = [begin]
    
    while True:
        #print(f"words : {words}")
        #print(f"answer : {answer + 1}")
        #print(f"nowArr : {nowArr}")
        nextArr = []
        if not nowArr:
            return 0
        answer = answer + 1
        while nowArr:
            now = nowArr.pop()
            if now == target:
                return answer
            else:
                for i, word in enumerate(words):
                    if similar(word, now):
                        nextArr.append(word)
                        words.pop(i)
        #print(f"nextArr : {nextArr}\n")
        nowArr = nextArr
