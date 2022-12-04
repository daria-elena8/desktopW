print("Introduceti numarul de valori:\n")
n=int(input())
print("Introduceti valorile:\n")
m1=0
m2=0
while n:
    x=int(input("x= "))
    if x>m1:
        m2=m1
        m1=x
    elif x>m2 & x!=m1:
        m2=x
    n=n-1
if m2==m1:
    print("Imposibil")
else:
    print(f"Cele mai mari doua numere din sir sunt {m1} si {m2}.")
