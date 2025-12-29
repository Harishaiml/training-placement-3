s=input()
c=0
for i in range(len(s)):
    for a,b in [(i,i),(i,i+1)]:
        while a>=0 and b<len(s) and s[a]==s[b]:
            c+=1
            a-=1;b+=1
print(c)
