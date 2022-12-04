import math
print("Introduceti coeficientii ecuatiei:\n")
a=int (input("a= "))
b=int (input("b= "))
c=int (input("c= "))

d=b*b-4*a*c

if d<0:
    print("Ecuatia nu are radacini reale\n")
elif d==0:
    print(f"Ecuatia este de gradul I, si are o singura radacina reala x={ (math.sqrt(d)-b)//2*a }.")
else:
    print(f"Ecuatia este de gradul II, si are doua radacini reale\nx1= {int( (math.sqrt(d)-b)//2*a) }\nx2= { int((-(math.sqrt(d))-b)//2*a)}")
