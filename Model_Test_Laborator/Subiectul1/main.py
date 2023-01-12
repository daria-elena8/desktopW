def citire_numere(f):
    linie=f.readline()
    while linie!="":
        l= linie.strip().split(" ")
        print(l)
        linie=f.readline()
    f.close()

f=open("numere.in", "r")
citire_numere(f)