# 입력
s = input()

# 자르는 횟수
count = 0

# s[i]와 s[i+1]을 비교했을 때 값이 다르면 자름
for i in range(len(s) - 1):
    if s[i] != s[i+1]:
        count += 1 # 자르는 횟수 +1

if count == 0: # 0인 경우에는 0
    print(count)
else: # 나머지 경우에는 (자르는 횟수 + 1) // 2
    print((count + 1) // 2)