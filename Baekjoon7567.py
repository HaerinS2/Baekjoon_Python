bo=input()
he=10
for i in range(1,len(bo)):
    if bo[i]==bo[i-1]:
        he+=5
    else:
        he+=10
print(he)
