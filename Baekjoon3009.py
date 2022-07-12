xli=[]
yli=[]
for i in range(3):
    x,y=map(int,input().split())
    xli.append(x)
    yli.append(y)
for i in range(3):
    if xli.count(xli[i])==1:
        x=xli[i]
    if yli.count(yli[i])==1:
        y=yli[i]
print(x, y)