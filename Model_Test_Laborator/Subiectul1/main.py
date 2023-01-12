doc=[]
l=[]
def citire_numere(f):
    line=f.readline()
    while line!="":
       l=line.strip().split(" ")
       doc.append(l)
       line=f.readline()

    f.close()

f=open("numere.in", "r")
citire_numere(f)
print(doc)