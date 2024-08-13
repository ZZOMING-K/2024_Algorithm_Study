
## < 13주차 회고 (해시(프로그래머스)) >
---
### [13주차] 해결한 과제
##### 타겟 넘버
- https://school.programmers.co.kr/learn/courses/30/lessons/43165

**<접근 방법>**  
  
- dfs로 풀었습니다. dfs 함수를 정의할 때, 함수 외부에서 정의된 answer는 nonlocal을 이용해서 접근할 수 있게 했고, 그 다음 수를 더하거나 빼는 두 가지 경우를 모두 고려해서 dfs를 수행했습니다.

---

##### 네트워크
- https://school.programmers.co.kr/learn/courses/30/lessons/43162

**<접근 방법>**  
  
- bfs로 풀었습니다. 다음 컴퓨터와 연결되어 있고(=`next_com = 1`) 아직 방문하지 않은 컴퓨터(=`visited[i] = False`)라면 방문 예약(`q.append(i)`)처리를 합니다. 이 때, 방문 예약 처리는 next_com 값이 아닌 **next_com**의 인덱스를 가지고 방문 예약을 합니다.
- 컴퓨터 개수만큼 for문을 돌면서 방문 처리가 되지 않은 컴퓨터라면 bfs를 수행하고, bfs가 종료될 때마다 answer를 1씩 증가시켜줍니다. bfs가 종료됐다는 것은 더 이상 연결된 것 노드가 없다는 의미이므로 이 때 하나의 네트워크라고 생각할 수 있습니다.

---

##### 게임 맵 최단거리
- https://school.programmers.co.kr/learn/courses/30/lessons/1844

**<접근 방법>**  
  
- bfs로 풀었습니다. 상하좌우로 한 칸씩 움직일 수 있게 dx, dy를 정의해주고 현재 위치에서 4 방향으로 움직이는 경우를 탐색합니다. 이 때, 이동할 위치가 맵 밖으로 벗어나거나 벽(=0)이라면 넘기고 갈 수 있는 곳이라면 해당 위치로 이동하면서 +1을 해줍니다. 그러면 최종적으로 도착해야 하는 위치(`maps[n-1][m-1]`)의 값은 얼마나 이동했는지를 저장하게 됩니다.
    - 만약에 도착할 수 없는 경우라면 그대로 1의 값을 갖고 있게 됩니다.


---

##### 단어 변환
- https://school.programmers.co.kr/learn/courses/30/lessons/43163

**<접근 방법>**  
  
- bfs로 풀었습니다. 주어진 단어들을 그래프로 나타내기 위해서 **"두 단어를 비교했을 때 글자가 한 개만 다른 경우에 두 단어가 이어져 있다"**고 생각했습니다. 그래서 두 단어를 비교하는 함수를 정의해주고, 그래프 구조로 나타내기 위해서 defaultdict를 활용했습니다. 이 때, queue 구조에 append를 할 때는 단어만 append 하는 것이 아니라 count 횟수도 같이 추가하고 다음 단어를 방문할 때 +1을 해줍니다.
    - 그리고 target 단어에 도달하면 해당 count를 반환해줍니다.


---
---
### [13주차] 해결하지 못한 과제
##### 여행 경로
- https://school.programmers.co.kr/learn/courses/30/lessons/43164

**<접근 방법>**  
  
- 테스트 케이스 1, 2 실패

---

##### 아이템 줍기
- https://school.programmers.co.kr/learn/courses/30/lessons/87694

**<접근 방법>**  
  


---

##### 퍼즐 조각 채우기
- https://school.programmers.co.kr/learn/courses/30/lessons/84021

**<접근 방법>**  
  

---
---
### [13주차] 처음 써본 함수 및 라이브러리


