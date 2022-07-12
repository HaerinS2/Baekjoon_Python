v=int(input())
ab=input()
if ab.count("A")<ab.count("B"):
    print("B")
elif ab.count("B")<ab.count("A"):
    print("A")
else:
    print("Tie")