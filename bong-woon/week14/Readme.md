
## < 14주차 회고 (힙(프로그래머스)) >
---
### [14주차] 해결한 과제
##### 더 맵게
- https://school.programmers.co.kr/learn/courses/30/lessons/42626

**<접근 방법>**  
  
- 스코빌지수가 담긴 리스트를 heapq로 바꾼 다음 `heappop`을 통해 스코빌지수가 가장 낮은 것부터 나오게 합니다. 
    - 만약에 가장 낮은 스코빌지수가 문제의 기준인 K보다 크거나 같다면 나머지 음식도 다 K보다는 크다는 의미이기 때문에 더 확인하지 않고 answer를 리턴합니다.
    - 아니라면 두번재로 낮은 스코빌지수도 추출한 다음 문제에서 제시한 공식대로 조합한 스코빌지수 값을 다시 heapq에 추가해주면서 answer += 1을 추가해줍니다. 

---

##### 이중우선순위큐
- https://school.programmers.co.kr/learn/courses/30/lessons/42628

**<접근 방법>**  
  
- heapq의 `nlargest`와 `nsmallest`를 이용해서 풀었습니다. 주어진 명령어를 공백 기준으로 분리해서 명령어의 시작이 "I"이면 heapq에 뒤의 숫자를 추가해주고, "D"인 경우는 '1' 혹은 '-1'인지를 확인하고 최댓값과 최솟값을 heapq에서 제거했습니다. 파이썬의 heapq는 min_heap 구조라서 최댓값을 제거할 때는 `nlargest`를 통해 최댓값을 찾고, `remove`를 통해 최댓값을 직접 제거해줬습니다.


---
---
### [14주차] 해결하지 못한 과제
##### 디스크 컨트롤러
- https://school.programmers.co.kr/learn/courses/30/lessons/42627

**<접근 방법>**  
  
- 


---
---
### [14주차] 처음 써본 함수 및 라이브러리


