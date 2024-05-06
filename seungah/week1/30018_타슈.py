'''
Q.30018:
1.대여소의 개수를 1번째,
2.서비스 전 각 대여소의 자전거 위치를 2번째,
3.서비스 후 바뀐 자전거의 개수를 3번째 열에 입력 후
4.원복하기 위한 최소 횟수 구하기.
    1. 대여소 자전거 댓수 비교
    2. 다르면 더하거나 뺄 횟수 count에 더하기
    3. 움직이는 횟수 move 구하기
5. 결과 출력
'''

station = int(input())  #1
a = list(map(int, input().split())) #2
b = list(map(int, input().split())) #3

count = 0 

for i in range(0, station):  #4
    if a[i] != b[i]:  #4-1
        count += abs(a[i] - b[i])  #4-2
move = int(count / 2)  #4-3

print(move)  #5

