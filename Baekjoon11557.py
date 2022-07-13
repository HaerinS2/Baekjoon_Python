t=int(input())
for _ in range(t):
    n=int(input())
    sL=[None]
    lL=[0]
    for _ in range(n):
        s,l=input().split()
        sL.append(s)
        lL.append(int(l))
    m=lL.index(max(lL))
    print(sL[m])