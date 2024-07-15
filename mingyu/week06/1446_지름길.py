#길이가 N일 때 최선이 무엇인지 확인하면서 진행해보자

#버려야 되는 지름길 존재
#1. 목적지를 초과한 지름길
#2. 시작, 도착이 같은데 비용이 큰 지름길
#3. 비용이 더 드는 지름길
#4. 시작 사이에 도착이 없고, 도착 사이에 시작이 없는 두 지름길 중 안의 지름길 길이가 더 긴 경우

#[[0, 0], [10, 9], [70, 64], [160, 148], [180, 162], [190, 174]는 들어가면 안됨], [900, 432]]

N, destination = map(int, input().split())
shortcut = []

for i in range(N):
    tmp = list(map(int, input().split()))
    if tmp[1] > destination or tmp[2] > tmp[1] - tmp[0]:
        continue
    shortcut.append(tmp)

shortcut.sort(key = lambda x:x[1])

distances = [[0, 0]]
#print(distances)
#print(shortcut)


for i in range(destination+1):
    while shortcut and shortcut[0][1] == i:
        if len(distances) == 1:
            distances.append([shortcut[0][1], shortcut[0][0] + shortcut[0][2]])
        else:
            distance = i
            for j in range(len(distances)):
                if distances[j][0] > shortcut[0][0]:
                    break
                if distances[j][1] + shortcut[0][0] - distances[j][0] + shortcut[0][2] < distance:
                    distance = distances[j][1] + shortcut[0][0] - distances[j][0] + shortcut[0][2]
                    #print(distance)
            if distance < i - distances[-1][0] + distances[-1][1]:
                #print(i)
                distances.append([i, distance])
        shortcut = shortcut[1:]
#print(distances)
print(destination - distances[-1][0] + distances[-1][1])
