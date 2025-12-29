a=list(map(int,input().split()))
mx=cur=a[0]
mn=cur2=a[0]
s=a[0]
for x in a[1:]:
    cur=max(x,cur+x)
    mx=max(mx,cur)
    cur2=min(x,cur2+x)
    mn=min(mn,cur2)
    s+=x
print(mx if mx<0 else max(mx,s-mn))
