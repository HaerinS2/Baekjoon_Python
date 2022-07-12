n=int(input())
li=[]
for i in range(n):
    li.append(int(input()))
if li.count(0)>li.count(1):
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")