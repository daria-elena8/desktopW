n=int(input("Va rog introduceti valoarea care trebuie verificata:\n"))
cn=n
m=0

while n:
    m=m*10+n%10
    n=n//10

if cn ==m:
    print(f"Numarul {cn} este palindrom")
else:
    print(f"Numarul {cn} nu este palindrom")