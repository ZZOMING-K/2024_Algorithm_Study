#모든 경우 전부 구해서 가장 작은 경우 출력해보자



def travel(left, cost, now):
    #print(now, left, cost)
    cp = left[:]
    cp.remove(now)
    
    if not cp:
        except_recall_cost.append([cost, now])
        #마지막 지점에서 시작 지점으로 오는 cost를 추가해야 함
        
    for j in cp:
        if distance[now][j] != 0:
            travel(cp, cost + distance[now][j], j)
            


N = int(input())
distance = []
answer = []
except_recall_cost = []
for i in range(N):
    distance.append(list(map(int, input().split())))


for i in range(N):
    travel([i for i in range(N)], 0, i)
    while except_recall_cost:
        now = except_recall_cost.pop()
        if distance[now[1]][i] != 0:
            answer.append(now[0] + distance[now[1]][i])

print(min(answer))

