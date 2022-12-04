n=int(input("Introduceti numarul de valori:\n"))
print(f"Introduceti cele {n} valori:\n")
max=0.0
x=float(input())
cn=n
n=n-1
zi=0
while n:
    y=float(input())
    if y>x:
        if max< y-x:
            max=y-x
            zi=cn-n
    elif x>y:
        if max< x-y:
            max=x-y
            zi=cn-n
    n=n-1
print(f"Cea mai mare diferenta s-a inregistrat in ziua {zi+1}, si a avut valoarea cu diferenta {max} fata de ziua anterioara")