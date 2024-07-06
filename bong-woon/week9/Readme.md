
## < 9주차 회고 (정렬(프로그래머스)) >
---
### [9주차] 해결한 과제
##### K번째수
- https://school.programmers.co.kr/learn/courses/30/lessons/42748

**<접근 방법>**  
  
- commands 리스트의 원소 [i, j, k]를 가지고 array를 [i-1 : j]로 슬라이싱을 합니다. 그리고 슬라이싱한 배열을 오름차순으로 정렬하고 [k-1]로 인덱싱을 하면 k번째 수가 됩니다.

---

##### H-Index
- https://school.programmers.co.kr/learn/courses/30/lessons/42747

**<접근 방법>**  
  
- max_h는 될 수 있는 H-Index의 최댓값입니다. 문제의 조건에 따라서 논문 n편을 발표한 과학자의 H-Index 최댓값은 각각 모두 n번 이상 인용됐다면 max_h = n이 됩니다. 즉, 발표한 논문의 개수가 그 과학자의 최대 H-Index 값입니다. max_h를 기준으로 citations 리스트에 있는 인용 횟수를 비교했을 때, 그 숫자가 max_h보다 크다면 count에 추가해서 그 개수를 셉니다.
- 그렇게 계산한 count가 max_h보다 크거나 같다면 이 때 max_h가 정답이 되고 아니라면 max_h 값을 1 줄여서 다시 같은 과정을 반복합니다.

---
---
### [9주차] 해결하지 못한 과제

##### 가장 큰 수
- https://school.programmers.co.kr/learn/courses/30/lessons/42746

**<접근 방법>**  
  
- 

---
---
### [9주차] 처음 써본 함수 및 라이브러리