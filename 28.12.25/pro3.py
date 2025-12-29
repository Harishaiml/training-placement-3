a=[1]+list(map(int,input().split()))+[1]
n=len(a)
dp=[[0]*n for _ in range(n)]
for l in range(2,n):
    for i in range(n-l):
        j=i+l
        dp[i][j]=max(a[i]*a[k]*a[j]+dp[i][k]+dp[k][j] for k in range(i+1,j))
print(dp[0][-1])
