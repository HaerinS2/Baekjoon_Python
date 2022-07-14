m=int(input());n=int(input())
mnList=[]
for i in range(m,n+1):
    root=int(i**(0.5))
    if root**2==i:
        mnList.append(i)
if len(mnList)!=0:
    print(sum(mnList))
    print(min(mnList))
else:
    print(-1)