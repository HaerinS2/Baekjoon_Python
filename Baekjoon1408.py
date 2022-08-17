this_h, this_m, this_s = map(int,input().split(":"))
start_h, start_m, start_s = map(int,input().split(":"))
rem = (start_h*3600 + start_m*60 + start_s) - (this_h*3600 + this_m*60 + this_s)

if rem < 0:
    rem += 3600*24

re_h = rem//3600
re_m = (rem%3600)//60
re_s = rem%60

print("%02d:%02d:%02d" %(re_h, re_m, re_s))