
## < 10주차 회고 (스택/큐(프로그래머스)) >
---
### [10주차] 해결한 과제
##### 같은 숫자는 싫어
- https://school.programmers.co.kr/learn/courses/30/lessons/12906

**<접근 방법>**  
  
- arr 배열의 첫번째 원소를 answer 리스트에 추가한 뒤, 그 다음 arr 원소부터는 answer 리스트의 마지막 원소와 비교합니다. 이 때, arr의 원소와 answer 리스트의 마지막 원소가 다른 경우에만 answer 리스트에 추가하면 같은 숫자가 연속해서 들어오는 것을 막게 됩니다.

---

##### 기능개발
- https://school.programmers.co.kr/learn/courses/30/lessons/42586

**<접근 방법>**  
  
- 먼저 입력으로 들어오는 리스트 progresses와 speeds를 큐 구조로 바꿔줍니다. progress_q가 비워질 때까지 아래 과정을 반복합니다.
    - 이 때, progress_q와 speed_q에서 각각 맨 앞의 원소를 가지고 현재 day와 계산했을 때 100보다 크거나 같으면 해당 작업은 완료가 됐다는 의미로 `popleft()`를 통해 큐에서 제거를 합니다. 그리고 작업이 완료됐다는 의미로 count도 +1 해줍니다.
        - popleft를 하고 난 뒤에 progress_q가 완전히 비었다면 현재 count를 answer에 추가합니다.
        - 반대로 progress_q의 원소가 남아있는 경우에는 progress_q와 speed_q의 첫번째 원소를 가지고 작업량을 계산했을 때 100보다 작으면 현재의 count를 answer에 추가합니다. 
    - 100보다 작은 경우에는 아직 작업이 완료가 안 됐기 때문에 day를 +1 해줍니다.

---

##### 올바른 괄호
- https://school.programmers.co.kr/learn/courses/30/lessons/12909

**<접근 방법>**  
  
- "("와 ")"를 순서대로 짝을 지어야 합니다. "(", ")" 는 유효한 괄호지만 ")", "("는 잘못된 괄호입니다.
- for문으로 입력된 문자열을 순회하면서 "("를 만나는 경우에는 리스트에 추가해주고 ")"를 만나는 경우에는 리스트에 담긴 "("를 하나씩 빼줍니다.
    - 이 때, ")"를 만나는 경우에는 리스트가 비어있을 수도 있고 비어있지 않을 수도 있는데 비어있지 않은 경우에는 "("와 함께 하나의 올바른 괄호를 완성한다는 의미입니다.
    - 하지만 리스트가 비어있다면 ")"의 짝인 "("가 없는 상태이므로 올바른 괄호가 되지 않습니다.

---

##### 프로세스
- https://school.programmers.co.kr/learn/courses/30/lessons/42587

**<접근 방법>**  

- 먼저 우선순위가 적힌 리스트와 현재 주어진 프로세스의 인덱스를 기억하기 위해서 인덱스도 리스트로 만든 뒤 둘다 큐 구조로 바꿉니다.
    - process_q에서 가장 우선순위가 큰 값과 순서상 첫번째 위치하는 프로세스의 우선순위를 비교했을 때, 첫번째 위치하는 프로세스의 우선순위가 max 값보다 크거나 같으면 프로세스를 처리한다는 의미로 `popleft()`를 합니다.
        - 이 때, 해당 프로세스의 인덱스가 location과 같으면 while문을 탈출하고 아닌 경우에는 다시 while문을 반복합니다.

---

##### 주식가격
- https://school.programmers.co.kr/learn/courses/30/lessons/42584

**<접근 방법>**  

- 가격 정보가 주어지는 리스트를 큐 구조로 바꾼 뒤, 큐에서 현재 확인할 가격을 `popleft()`로 뽑고, 나머지 가격들과 비교를 합니다.
    - 비교를 했을 때 현재 확인하는 가격이 나머지 가격보다 크거나 같은 경우에만 count를 1 증가시켜주고 작은 경우에도 count를 1 증가시켜준 뒤 for문을 탈출합니다.
        - 바로 다음 시점에 가격이 떨어지더라도 1초간은 가격이 떨어지지 않은 것으로 보기 때문에 작은 경우에도 count를 1 증가시켜줍니다.


---
---
### [10주차] 해결하지 못한 과제

##### 다리를 지나는 트럭
- https://school.programmers.co.kr/learn/courses/30/lessons/42583

**<접근 방법>**  

- 


---
---
### [10주차] 처음 써본 함수 및 라이브러리
