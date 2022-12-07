n=float(input("n= "))
c=1
cm=0
maxi=0
x=float(input("x= "))
n=n-1
while n:
    y=float(input("y= "))
    if y>x and y-x>maxi:
        maxi=y-x
        cm=c
    x=y
    n=n-1
    c=c+1
print(f"cea mai mare diferenta a fost inregistrata intre zilele {cm} si {cm+1}, iar valoarea acesteia este de {round(maxi,2)} ")


