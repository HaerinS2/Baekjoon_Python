while True:
    n=int(input())
    if n==-1:
        break
    ns=[0]
    for i in range(2, n):
        if n%i==0:
            ns.append(i)
    if sum(ns)+1==n:
        res=str(n)+" = "+"1"
        for j in range (1, len(ns)):
            res+=" + "+str(ns[j])
        print(res)
    else:
        print(n,"is NOT perfect.")