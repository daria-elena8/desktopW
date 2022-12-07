
x=int(input("lungimea initiala a sariturii: "))
n=int(input("saritura greierului se miscoreaza o data la: "))
p=int(input("procentajul cu care se micsoreaza saritura greierului de fiecare data: "))
m=int(input("numarul de sarituri pe care le face greirele: "))
dist=0
while m>n:
    dist=dist+(m-n)*x
    m=m-n
    x= (100-p)*x//100


dist=dist+m*x
print(f"distanta pe care a parcurs-o greierul este de {dist} cm")

