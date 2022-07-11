a,b,c=map(int,input().split())
d=int(input())

second=(c+d)%60
m1=(c+d)//60

minute=(b+m1)%60
h1=(b+m1)//60

hour=(a+h1)%24

print(hour, minute, second)