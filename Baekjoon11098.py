n=int(input())
for _ in range(n):
    p=int(input())
    dic={}
    for _ in range(p):
        c,n=map(str,input().split())
        dic[int(c)]=n
    print(dic.get(max(dic.keys())))