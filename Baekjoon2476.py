result=[]
n=int(input())
for i in range(n):
    dice=list(map(int,input().split()))
    if dice[0]==dice[1]==dice[2]:
        result.append(10000+dice[0]*1000)
    elif dice[0]==dice[1] or dice[0]==dice[2]:
        result.append(1000+dice[0]*100)
    elif dice[1]==dice[2]:
        result.append(1000+dice[1]*100)
    else:
        dice.sort()
        result.append(dice[-1]*100)
result.sort()
print(result[-1])