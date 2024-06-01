import sys
dp = [0 for _ in range(301)]
a = [0 for _ in range(301)] 

n = int(sys.stdin.readline()) 

for i in range(1 , n+1) :
	a[i] = int(sys.stdin.readline()) 

dp[1] = a[1] 
dp[2] = a[1] + a[2] 
dp[3] = max(a[1] + a[3]  , a[2] + a[3] )
for i in range(4 , n+1) :
	dp[i] = max(a[i] + a[i-1] + dp[i-3] , a[i] + dp[i-2] ) 
	
print(dp[i]) 