n= int(input("n= "))
cn=n
m=0
while cn!=0:
    m= 10*m +(cn%10)
    cn=cn//10
print(m)
if n!=m:
    print("nu este palindrom")
else:
    print("este palindrom")