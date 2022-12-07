import math
a=int(input("a= "))
b=int(input("b= "))
c=int(input("c= "))
d=int(b*b-4*a*c)
print(f"delta este {d}")
if d>0:
  print(f"are doua radini reale, aceste sunt:\n x1= {int((-math.sqrt(d)-b))//2*a}\n x2= {int(math.sqrt(d)-b)//2*a}\n ")
elif d==0:
    print(int(math.sqrt(d)))
    print(f"are o radacina reala, aceasta este:\n x= {b//2*a}\n")
else:
    print("nu are radacini reale")