n=int(input("n= "))
maxi1=0
maxi2=0
while n:
    x=int(input("x= "))
    if x>maxi1:
        maxi1=x
    if x>maxi2 and x!=maxi1:
        maxi2=x
    n=n-1
if maxi1==0 or maxi2==0:
    print("imposibil")
else:
    print(f"cea mai mare valoare este {maxi1}, iar urmatoarea este {maxi2}")