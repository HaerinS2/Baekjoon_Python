n=int(input())
x_sc=100; y_sc=100;
for _ in range(n):
    x,y=map(int,input().split())
    if x>y:
        y_sc-=x
    elif y>x:
        x_sc-=y
print(x_sc, y_sc,sep="\n")