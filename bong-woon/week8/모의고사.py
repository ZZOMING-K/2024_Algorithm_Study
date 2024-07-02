def solution(answers):
    answer = []
    num_problem = len(answers) # 주어지는 문제 숫자

    student1 = [1, 2, 3, 4, 5] * 2000
    student2 = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000

    # 학생별 정답을 맞춘 문제수
    count1 = 0
    count2 = 0
    count3 = 0

    for s1, s2, s3, ans in zip(student1[:num_problem], student2[:num_problem], student3[:num_problem], answers):
        if ans == s1:
            count1 += 1
        if ans == s2:
            count2 += 1
        if ans == s3:
            count3 += 1

    count_lst = [count1, count2, count3]
    for i, cnt in enumerate(count_lst):
        if max(count_lst) == cnt: # 맞춘 문제의 최댓값과 같으면 answer 리스트에 추가
            answer.append(i + 1)

    return answer