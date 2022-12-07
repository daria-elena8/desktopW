n=int(input("Introduceti numarul:\n"))
p=10
cn=n
cmin=9
poz=0
i=10

while cn:

    if cn%10<cmin:
        cmin=cn%10
        poz=i
    i = i * 10
    cn=cn//10





print(n)
