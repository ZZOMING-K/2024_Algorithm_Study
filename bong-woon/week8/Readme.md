
## < 8주차 회고 (완전 탐색(프로그래머스)) >
---
### [8주차] 해결한 과제
##### 최소직사각형
- https://school.programmers.co.kr/learn/courses/30/lessons/86491

**<접근 방법>**  
  
- 명함의 크기가 \[가로, 세로\]로 주어지는데 가로가 큰 경우도 있고 세로가 큰 경우가 있습니다. 명함을 눕혀서 수납할 수도 있기 때문에 세로가 큰 경우는 가로, 세로의 값을 바꿔서 명함이 항상 가로가 긴 방향으로 수납하게끔 통일시킵니다. 그래서 가장 긴 가로 길이와 가장 긴 세로 길이를 곱한 값을 최소 지갑의 크기라고 생각할 수 있습니다.

---

##### 모의고사
- https://school.programmers.co.kr/learn/courses/30/lessons/42840

**<접근 방법>**  
  
- 각 학생별로 문제 찍는 패턴를 리스트로 10,000개 만들어둡니다. 그리고 입력으로 들어오는 문제 수만큼 리스트를 자르고, 주어진 문제의 답과 비교하면서 정답과 같은 경우에 count 개수를 각각 늘려줍니다. 그리고 최종적으로 그 중에서 문제를 가장 많이 맞힌 학생의 번호를 answer 리스트에 추가합니다.

---

##### 소수찾기
- https://school.programmers.co.kr/learn/courses/30/lessons/42839

**<접근 방법>**  
  
- `from itertools import permutations` 라이브러리를 활용했습니다. 문제의 예시처럼 "17"이 주어졌을 때, "1", "7"을 뽑아서 "17"을 만드는 것과 "7", "1"을 뽑아서 "71"을 만드는 것은 다르기 때문에 뽑는 순서가 중요한 순열 문제라고 생각했습니다.
- 주어진 문자열의 길이만큼 permutation을 반복하고, 각각의 permutation된 결과를 숫자 하나씩 이어붙이고 정수형으로 변환해준 뒤, 모두 prime_lst에 추가해줬습니다. 그리고 리스트에 담긴 숫자가 소수인지 확인하고 소수가 맞다면 answer에 1을 더해주면서 소수의 개수를 출력하게 했습니다.

---

##### 카펫
- https://school.programmers.co.kr/learn/courses/30/lessons/42842

**<접근 방법>**  

- 갈색 격자와 노란색 격자의 크기가 각각 가로, 세로가 1인 정사각형이라고 한다면 갈색 격자와 노란색 격자의 개수가 카펫의 넓이가 됩니다.
- 1부터 카펫의 넓이까지 for문을 돌면서 카펫의 넓이를 for문을 도는 숫자로 나눴을 때, 정수로 나누어 떨어지는 경우만 살펴보면 됩니다.
    - 이 때 카펫은 항상 가로가 세로보다 크거나 같기 때문에 넓이를 i로 나눈 몫이 나누는 숫자 i보다 크다면 나눈 몫이 가로가 되고, 나누는 숫자가 세로가 됩니다.
    - 갈색 격자는 노란색 격자 외부에 한 줄만 테두리로 쓰이기 때문에 카펫 내부의 노란색 격자로 이루어진 구역의 가로 세로 길이는 원래 카펫의 가로 세로 길이보다 2씩 짧아집니다. 그러므로 계산한 (w - 2 ), (h - 2)의 곱이 노란색 격자 수와 같다면, 그 w와 h가 카펫의 가로 세로 길이가 됩니다.

---

##### 피로도
- https://school.programmers.co.kr/learn/courses/30/lessons/87946

**<접근 방법>**  

- 던전을 방문하는 모든 경우의 수를 고려하기 위해서 `from itertools import permutations`를 이용했습니다. 현재 피로도가 입장하기 위한 최소 피로도보다 크면 count를 1 증가 시켜주고, 현재 피로도에서 소모 피로도만큼 감소시킵니다. 각 경우의 수에 속하는 던전을 모두 순회하면 계산된 던전의 방문 횟수를 count_lst에 담고, count_lst의 최댓값을 구하면 주어진 피로도와 던전으로 방문할 수 있는 최대 횟수가 됩니다.  

---

##### 모음사전
- https://school.programmers.co.kr/learn/courses/30/lessons/84512

**<접근 방법>**  

- 처음에는 `combinations_with_replacement`를 이용해서 모든 경우의 수를 구하려고 했으나 3번째 테스트 케이스부터 틀렸다고 출력이 됐습니다. 그래서 경우의 수가 몇 가지인지 확인해보니 251로 제가 생각한 경우의 수보다 훨씬 적었습니다. 왜 생각한 숫자만큼 안 나오는지 확인하기 위해서 combination의 결과를 출력해보니까 combinations의 경우 기본적으로 순서를 고려하지 않기 때문에 "A, E"나 "E, A"나 같은 경우로 판단하기 때문에 제가 생각했던 경우의 수보다 훨씬 적게 나온다는 것을 알게 되었습니다.
- 그래서 itertools의 또 다른 라이브러리인 `from itertools import product` 라이브러리를 활용했습니다. 이 라이브러리는 순서와 중복을 모두 고려한 경우의 수를 구해줍니다. `permutation`도 순서를 고려한 조합이지만 permutation은 중복을 허용하지 않습니다. "A, E"가 주어져 있다면 "AE", "EA"만 경우의 수로 생각하지 "AA", "EE"는 고려하지 않기 때문에 product를 활용했습니다.

---
---
### [8주차] 해결하지 못한 과제

##### 전력망을 둘로 나누기
- https://school.programmers.co.kr/learn/courses/30/lessons/86971

**<접근 방법>**  

- 


---
---
### [8주차] 처음 써본 함수 및 라이브러리
#### permutations, combinations, combinations_with_replacement, product
- 4가지 모두 경우의 수를 쉽게 고려할 수 있게 도와주지만 차이가 있습니다.
```python
from itertools import permutations, combinations, combinations_with_replacement, product

lst = [1, 2, 3]

perm = permutations(lst, 2)
comb = combinations(lst, 2)
comb_replace = combinations_with_replacement(lst, 2)
prod = product(lst, repeat = 2)

# permutation : 순서 고려 O, 중복 허용 X
for i in perm:
    print(i) # (1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)

# combinations : 순서 고려 X, 중복 허용 X
for i in comb:
    print(i) # (1, 2), (1, 3), (2, 3)

# combinations_with_replacement : 순서 고려 X, 중복 허용 O
for i in comb_replace:
    print(i) # (1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)

# product : 순서 고려 O, 중복 허용 O
for i in prod:
    print(i) # (1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)

```