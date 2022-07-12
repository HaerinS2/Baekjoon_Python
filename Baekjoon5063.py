n=int(input())
for i in range(n):
    r,e,c=map(int,input().split())
    if r<e-c:
        print('advertise')
    elif e-c<r:
        print('do not advertise')
    else:
        print('does not matter')