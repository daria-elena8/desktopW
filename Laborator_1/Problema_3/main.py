print("Va rugam sa introduceti valorile pentru lungime si latime:\n")
L1=int(input("L1= "))
L2=int(input("L2= "))

A=L1*L2
d=A//2
while d>=2:
    if A%(d*d)==0:
        print(f"Sunt necesare {A//(d*d)} placi de gresie cu latura de {d} cm\n ")
        break
    d=d-1
