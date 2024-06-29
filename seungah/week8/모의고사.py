
def solution(answers):
    def cyclic_list(num, leng):
        return num * (leng // len(num)) + num[:leng % len(num)]

    students = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    count = [0, 0, 0]
    stuanswer = [[],[],[]]  

    
    for i in range(3):  
        stuanswer[i] = cyclic_list(students[i], len(answers))

        for j in range(len(answers)):
            if answers[j] == stuanswer[i][j]:
                count[i] += 1

    max_count = max(count)
    #여기에서 헤맴
    result = [i + 1 for i, v in enumerate(count) if v == max_count]
    return result


