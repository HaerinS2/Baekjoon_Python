a=int(input())
b=int(input())
b1=int(b/100) # 백의 자리
b2=b%10 # 일의 자리
b3=int((b%100)/10) # 십의 자리

print(a*b2,a*b3,a*b1,a*b,sep='\n')