n=int(input())
for i in range(n):
    ox=input()
    c=0
    sum=0
    for i in range(len(ox)):
        if ox[i]=='O':
            c+=1; sum+=c
        else:
            c=0
    print(sum)