length, start = map(int, input().split())
fruits = list(map(int, input().split()))

fruits.sort()

for i in range(length):
    if fruits[i] <= start:
        start += 1
    elif fruits[i] > start:
        break

print(start)

'''
https://www.acmicpc.net/problem/16435

length : 과일의 개수
start  : 스네이크버드의 초기 길이
fruits : 과일들

과일 개수만큼 반복문을 돌리면서,
스네이크버드의 길이보다 과일의 크기가 작거나 같으면 +1
과일 크기가 더 커지는 순간, break로 종료
'''