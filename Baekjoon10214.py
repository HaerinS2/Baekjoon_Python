# y=yonsei, k=korea
t=int(input())
for _ in range(t):
    y_sc=k_sc=0
    for _ in range(9):
        y,k=map(int,input().split())
        y_sc+=y
        k_sc+=k    
    if y_sc==k_sc:
        print("Draw")
    elif y_sc>k_sc:
        print("Yonsei")
    else:
        print("Korea")