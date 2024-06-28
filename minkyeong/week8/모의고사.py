def solution(answers):
    #수포자1 정답 리스트 생성 
    num1 = [1,2,3,4,5]  
    num1 = num1 * (len(answers) // len(num1)) + num1[:(len(answers) % len(num1))+1]
    #수포자2 정답 리스트 생성 
    num2 = [2,1,2,3,2,4,2,5] 
    num2 = num2 * (len(answers) // len(num2)) + num2[:(len(answers) % len(num2))+1]
    #수포자3 정답 리스트 생성 
    num3 = [3,3,1,1,2,2,4,4,5,5] 
    num3 = num3 * (len(answers) // len(num3)) + num3[:(len(answers) % len(num3))+1]
    
    score = [0,0,0] # 수포자들 정답 개수 
    
    for idx , value in enumerate(answers) : #만일 수포자들 답 - 해당 문제 답 = 0 이 될 경우 정답으로 간주하고 count
        if num1[idx] - value == 0 :
            score[0] += 1
        if num2[idx] - value == 0 :
            score[1] += 1 
        if num3[idx] - value == 0 :
            score[2] += 1
    
    max_score = max(score) #score 최대값 
    answer = [idx+1 for  idx , s in enumerate(score) if s == max_score] #score리스트에 최대값인 인덱스 추출 
    return answer 