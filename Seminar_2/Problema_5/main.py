sir=input("Va rog introduceti sirul: \n")

ok=0
i=1
while i<=len(sir)//2:
    if len(sir)%i==0:
        a=sir[:i]*(len(sir)//(i))
        print(a)
        if a == sir:
            print(f"S-a gasit un subsir din care se poate forma sirul. Acesta este {a} si este nevoie sa apara de {(len(sir))//i} ori pentru a forma sirul")
            ok=1
            break
    i=i+1


if ok==0:
    print("Nu s-a gasit un subsir care sa respecte proprietatea ceruta")
