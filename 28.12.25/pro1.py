n,m=map(int,input().split())
p=list(range(n*m))
r=[0]*(n*m)
g=[0]*(n*m)
def f(x):
    if p[x]!=x:p[x]=f(p[x])
    return p[x]
def u(a,b):
    a,b=f(a),f(b)
    if a!=b:
        if r[a]<r[b]:a,b=b,a
        p[b]=a
        if r[a]==r[b]:r[a]+=1
cnt=0
for _ in range(int(input())):
    i,j=map(int,input().split())
    x=i*m+j
    if g[x]:print(cnt);continue
    g[x]=1
    cnt+=1
    for di,dj in [(1,0),(-1,0),(0,1),(0,-1)]:
        ni,nj=i+di,j+dj
        y=ni*m+nj
        if 0<=ni<n and 0<=nj<m and g[y] and f(x)!=f(y):
            u(x,y)
            cnt-=1
    print(cnt)
