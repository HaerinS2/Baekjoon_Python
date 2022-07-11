t=int(input())
for _ in range(t):
    r,s=input().split()
    r=int(r)
    text=''
    for i in s:
        text+=i*r
    print(text)