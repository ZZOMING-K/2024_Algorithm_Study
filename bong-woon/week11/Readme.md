
## < 11주차 회고 (해시(프로그래머스)) >
---
### [11주차] 해결한 과제
##### 폰켓몬
- https://school.programmers.co.kr/learn/courses/30/lessons/1845

**<접근 방법>**  
  
- 입력된 몬스터의 수와 그 중에서 고유한 몬스터의 종류의 수를 각각 계산합니다.
    - 고유한 몬스터의 종류가 입력된 몬스터 수의 절반보다 작은 경우에는 정답이 고유한 몬스터의 종류 수가 정답이 되고
    - 아닌 경우에는 모든 몬스터의 수의 절반이 정답이 됩니다.

---

##### 완주하지 못한 선수
- https://school.programmers.co.kr/learn/courses/30/lessons/42576

**<접근 방법>**  
  
- 문제의 조건상 완주하지 못하는 사람은 항상 한 명 뿐이므로 참가자 리스트와 완주자 리스트를 정렬한 뒤 
- **참가자 리스트에서 마지막 원소를 제외한 리스트와 완주자 리스트의 원소**를 비교하면서 다른 경우에는 그 이름이 완주하지 못한 사람의 이름이 됩니다.
- 만약 for문을 다 도는 동안에도 다른 경우가 없다면 **참가자 리스트의 마지막 원소**가 완주하지 못한 사람의 이름입니다.

---

##### 전화번호 목록
- https://school.programmers.co.kr/learn/courses/30/lessons/42577

**<접근 방법>**  
  
- 처음에는 phone_number 리스트를 문자열 길이 기준으로 오름차순 정렬해서 풀려고 했는데 이 경우에는 이중 for문을 써야되서 시간 초과 문제가 발생했습니다.
- 그래서 phone_number를 단순하게 문자열 기준으로 오름차순 정렬을 하면 사전처럼 정렬이 되서 앞에 시작하는 숫자가 비슷한 번호끼리 모여 있게 되고(ex. 111, 112, 113), 또 길이가 짧은 번호가 앞에 오게 정렬이 됩니다.(ex. 123, 1230)
    - for 문을 한 번만 이용해서 현재 번호가 바로 뒤의 번호의 접두어가 되는지 확인하면서 그런 경우가 있다면 False를 반환하고 for문을 종료합니다.


---

##### 의상
- https://school.programmers.co.kr/learn/courses/30/lessons/42578

**<접근 방법>**  
  
- defaultdict를 이용해서 옷의 종류에 따라 몇 개가 있는지를 셉니다. 입력이 [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]라면 "headgear" : 2, "eyewear" : 1이 됩니다.
- 이 때, 의상을 입는 경우의 수는 각각의 종류에 대해서 (2 + 1) x (1 + 1) = 6이 됩니다. 해당 종류의 옷을 입지 않은 경우도 생각해야 하기 때문에 +1을 해줬습니다. 하지만 이렇게 계산하면 아무것도 입지 않은 경우도 경우의 수에 포함되기 때문에 "최소 한 개의 의상은 입는다"는 조건상 아무것도 입지 않는 경우 한 가지를 빼줘야 하므로 6 - 1 = 5가 됩니다.
    - 그래서 defaultdict에 담긴 values에 1을 더한 뒤 모두 곱해주고 마지막에 1을 빼면 정답이 됩니다
    - 단, 의상의 종류가 한 가지인 경우에는 values 그 자체가 정답이 됩니다.

---

##### 베스트앨범
- https://school.programmers.co.kr/learn/courses/30/lessons/42579

**<접근 방법>**  
  
- idx_lst는 주어진 입력에 대한 인덱스 정보를 담은 리스트이고, song_lst는 각 노래의 [장르, 재생횟수, 고유번호(인덱스)]를 원소로 가지는 리스트입니다.
- 첫번째 defaultdict(song_dict)는 장르별 총 재생횟수를 저장하기 위한 딕셔너리입니다.
    - 이 두 가지를 가지고 먼저 song_lst를 내림차순으로 정렬해줍니다. 정렬 기준은 **장르별 총 재생횟수**와 **각 노래별 재생횟수** 두 가지입니다.

- 두번째 defaultdict(song_count)는 장르별 곡의 개수를 2개로 제한하기 위한 딕셔너리입니다.
    - 정렬된 song_lst를 for문으로 순회하면서 song_count를 채워주는데, 이 때 Key는 장르, Value는 장르별 곡의 개수입니다.
    - 해당 장르의 곡의 개수가 2보다 작은 경우에만 +1을 해주면서 answer 리스트에 해당 곡의 고유번호를 차례대로 append 해줍니다.



---
---
### [11주차] 해결하지 못한 과제


---
### [11주차] 처음 써본 함수 및 라이브러리

#### defaultdict
```python
from collections import defaultdict

d = defaultdict(int) # defalutdict(type), value 값이 기본적으로 0
d['a'] += 1
d['b'] += 10
print(d) # {'a' : 1, 'b' : 10}
print(d['c']) # 0


d = defaultdict(float) # default : '0.0'
d['a'] += 1
d['b'] += 10
print(d) # {'a' : 1.0, 'b' : 10.0}
print(d['c']) # 0.0


d = defaultdict(str) # default : ''
d['random'] += 'a'
d['xyz'] += 'b'
print(d) # {'random' : 'a', 'xyz' : 'b'}
print('empty:', d['c']) # empty : 


d = defaultdict(list) # default : []
d['x'] += [1, 2]
print(d) # {'x' : [1, 2]}
print(d['c']) # []
```
